#!/usr/bin/env python3
"""nandcheck - sanity-check Xbox 360 NAND dumps before you trust them.

A NAND dump is the only way back if a hardware mod goes wrong, so it is
worth checking that it is complete and that repeated dumps agree before
building or flashing anything from it.

Usage:
    python nandcheck.py info      nanddump1.bin
    python nandcheck.py compare   nanddump1.bin nanddump2.bin [more.bin ...]
    python nandcheck.py strip-ecc nanddump1.bin nanddump1_noecc.bin
    python nandcheck.py smc       nanddump1.bin smc_decrypted.bin

Exit status: 0 = looks fine, 1 = problems found, 2 = bad usage / unreadable file.
Only uses the Python standard library (Python 3.8+).
"""

import argparse
import hashlib
import os
import struct
import sys

PAGE = 0x200    # data bytes per NAND page
SPARE = 0x10    # ECC/spare bytes stored after each page in a raw dump
RAW_PAGE = PAGE + SPARE
BLOCK_PAGES = 32  # pages per 16KB small-block erase block; used as the compare unit

# Dump sizes the common dumping tools produce. (description, has ECC spare)
KNOWN_SIZES = {
    0x1080000: ("16MB NAND with ECC spare (Trinity, 16MB Corona, and older 16MB boards)", True),
    0x1000000: ("16MB NAND without ECC spare", False),
    0x4200000: ("64MB system area with ECC spare (256/512MB big-block NAND)", True),
    0x4000000: ("64MB system area without ECC spare", False),
    0x10800000: ("full 256MB NAND with ECC spare", True),
    0x21000000: ("full 512MB NAND with ECC spare", True),
    0x3000000: ("48MB MMC/eMMC system area (4GB-model boards, no ECC spare)", False),
}

RETAIL_MAGIC = 0xFF4F
SMC_KEY = (0x42, 0x75, 0x4E, 0x79)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def detect_layout(size):
    """Return (description, has_spare, recognised) for a dump of `size` bytes."""
    if size in KNOWN_SIZES:
        desc, spare = KNOWN_SIZES[size]
        return desc, spare, True
    # Unrecognised: guess from which page size divides evenly.
    spare = size % RAW_PAGE == 0 and size % PAGE != 0
    return "unrecognised size", spare, False


def strip_ecc(raw):
    """Drop the 16 spare bytes after every 512-byte page."""
    mv = memoryview(raw)
    return b"".join(mv[i:i + PAGE] for i in range(0, len(mv), RAW_PAGE))


def read_logical(f, offset, length, has_spare):
    """Read `length` bytes at data offset `offset`, skipping spare bytes if present."""
    if not has_spare:
        f.seek(offset)
        return f.read(length)
    first_page = offset // PAGE
    last_page = (offset + length + PAGE - 1) // PAGE
    f.seek(first_page * RAW_PAGE)
    data = strip_ecc(f.read((last_page - first_page) * RAW_PAGE))
    start = offset - first_page * PAGE
    return data[start:start + length]


def smc_decrypt(data):
    key = list(SMC_KEY)
    out = bytearray(len(data))
    for i, b in enumerate(data):
        mod = b * 0xFB
        out[i] = b ^ key[i & 3]
        key[(i + 1) & 3] = (key[(i + 1) & 3] + mod) & 0xFF
        key[(i + 2) & 3] = (key[(i + 2) & 3] + (mod >> 8)) & 0xFF
    return bytes(out)


def smc_encrypt(data):
    key = list(SMC_KEY)
    out = bytearray(len(data))
    for i, b in enumerate(data):
        enc = b ^ key[i & 3]
        mod = enc * 0xFB
        out[i] = enc
        key[(i + 1) & 3] = (key[(i + 1) & 3] + mod) & 0xFF
        key[(i + 2) & 3] = (key[(i + 2) & 3] + (mod >> 8)) & 0xFF
    return bytes(out)


def parse_header(hdr):
    """Parse the fields of the 0x80-byte flash header that this tool uses."""
    magic, build = struct.unpack_from(">HH", hdr, 0x00)
    (cb_offset,) = struct.unpack_from(">I", hdr, 0x08)
    copyright_ = hdr[0x10:0x50].split(b"\x00", 1)[0].decode("latin-1", "replace")
    (kv_offset,) = struct.unpack_from(">I", hdr, 0x6C)
    smc_length, smc_offset = struct.unpack_from(">II", hdr, 0x78)
    return {
        "magic": magic,
        "build": build,
        "cb_offset": cb_offset,
        "copyright": copyright_,
        "kv_offset": kv_offset,
        "smc_length": smc_length,
        "smc_offset": smc_offset,
    }


def inspect(path):
    """Return (info dict, list of problems) for one dump."""
    problems = []
    with open(path, "rb") as f:
        f.seek(0, 2)
        size = f.tell()
        desc, has_spare, recognised = detect_layout(size)
        info = {"path": path, "size": size, "layout": desc, "has_spare": has_spare}
        if not recognised:
            problems.append(f"size {size:#x} doesn't match any known dump size; the dump may be truncated")
        if size < RAW_PAGE:
            problems.append("file is too small to be a NAND dump")
            return info, problems

        hdr = read_logical(f, 0, 0x80, has_spare)
        first_page = read_logical(f, 0, PAGE, has_spare)
        if first_page in (b"\x00" * PAGE, b"\xff" * PAGE):
            problems.append("first page is blank (all 00 or all FF): the read failed")
            return info, problems

        h = parse_header(hdr)
        info["header"] = h
        if h["magic"] != RETAIL_MAGIC:
            problems.append(f"header magic is {h['magic']:#06x}, expected {RETAIL_MAGIC:#06x} for a retail console")
        if "Microsoft" not in h["copyright"]:
            problems.append("copyright string missing from header; the start of the dump is likely corrupt")

        data_size = size // RAW_PAGE * PAGE if has_spare else size
        smc_end = h["smc_offset"] + h["smc_length"]
        if not 0 < h["smc_length"] <= 0x4000 or smc_end > data_size:
            problems.append(f"SMC location looks wrong (offset {h['smc_offset']:#x}, length {h['smc_length']:#x})")
        else:
            info["smc"] = read_logical(f, h["smc_offset"], h["smc_length"], has_spare)
    return info, problems


def cmd_info(args):
    try:
        info, problems = inspect(args.dump)
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    print(f"File:     {info['path']}")
    print(f"Size:     {info['size']:,} bytes ({info['size']:#x})")
    print(f"Layout:   {info['layout']}")
    print(f"ECC:      {'present' if info['has_spare'] else 'not present'}")
    h = info.get("header")
    if h:
        print(f"Magic:    {h['magic']:#06x}")
        print(f"Build:    {h['build']}")
        print(f"Header:   {h['copyright']}")
        print(f"CB at:    {h['cb_offset']:#x}")
        print(f"KV at:    {h['kv_offset']:#x}")
        print(f"SMC at:   {h['smc_offset']:#x}, {h['smc_length']:#x} bytes")
    if "smc" in info:
        print(f"SMC hash: {hashlib.sha256(info['smc']).hexdigest()[:16]}... (encrypted)")
    print(f"SHA-256:  {sha256_file(args.dump)}")
    print()
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("Structure looks OK. This can't prove the dump is error-free: compare it")
    print("against at least one more dump with `nandcheck.py compare`.")
    return 0


def cmd_compare(args):
    paths = args.dumps
    try:
        sizes = {p: os.path.getsize(p) for p in paths}
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    if len(set(sizes.values())) != 1:
        print("Dumps are different sizes, so they can't be the same NAND:")
        for p, s in sizes.items():
            print(f"  {s:>12,}  {p}")
        return 1

    size = sizes[paths[0]]
    _, has_spare, _ = detect_layout(size)
    block = BLOCK_PAGES * (RAW_PAGE if has_spare else PAGE)
    handles = [open(p, "rb") for p in paths]
    hashes = [hashlib.sha256() for _ in paths]
    bad_blocks = []
    try:
        index = 0
        while True:
            chunks = [h.read(block) for h in handles]
            if not chunks[0]:
                break
            for hsh, c in zip(hashes, chunks):
                hsh.update(c)
            if any(c != chunks[0] for c in chunks[1:]):
                bad_blocks.append(index)
            index += 1
    finally:
        for h in handles:
            h.close()

    for p, hsh in zip(paths, hashes):
        print(f"{hsh.hexdigest()}  {p}")
    print()
    if not bad_blocks:
        print(f"All {len(paths)} dumps are identical. Keep copies in at least two places.")
        return 0
    shown = ", ".join(f"{b:#x}" for b in bad_blocks[:16])
    more = f" (+{len(bad_blocks) - 16} more)" if len(bad_blocks) > 16 else ""
    print(f"MISMATCH in {len(bad_blocks)} block(s) of {block:#x} bytes: {shown}{more}")
    print("Don't use these dumps. Check the reader's connection and dump again.")
    return 1


def cmd_strip_ecc(args):
    try:
        with open(args.dump, "rb") as f:
            raw = f.read()
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    _, has_spare, _ = detect_layout(len(raw))
    if not has_spare:
        print("This dump has no ECC spare data; nothing to strip.", file=sys.stderr)
        return 1
    data = strip_ecc(raw)
    with open(args.out, "wb") as f:
        f.write(data)
    print(f"Wrote {len(data):,} bytes to {args.out}")
    return 0


def cmd_smc(args):
    try:
        info, problems = inspect(args.dump)
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    if "smc" not in info:
        print("Couldn't locate the SMC in this dump:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1
    dec = smc_decrypt(info["smc"])
    with open(args.out, "wb") as f:
        f.write(dec)
    print(f"Wrote decrypted SMC ({len(dec):#x} bytes) to {args.out}")
    print(f"SHA-256: {hashlib.sha256(dec).hexdigest()}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Sanity-check Xbox 360 NAND dumps.")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("info", help="show layout and header details, flag obvious corruption")
    p.add_argument("dump")
    p.set_defaults(func=cmd_info)

    p = sub.add_parser("compare", help="check that two or more dumps are byte-identical")
    p.add_argument("dumps", nargs="+")
    p.set_defaults(func=cmd_compare)

    p = sub.add_parser("strip-ecc", help="write a copy with the ECC spare bytes removed")
    p.add_argument("dump")
    p.add_argument("out")
    p.set_defaults(func=cmd_strip_ecc)

    p = sub.add_parser("smc", help="extract and decrypt the SMC firmware")
    p.add_argument("dump")
    p.add_argument("out")
    p.set_defaults(func=cmd_smc)

    args = parser.parse_args(argv)
    if args.command == "compare" and len(args.dumps) < 2:
        parser.error("compare needs at least two dumps")
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
