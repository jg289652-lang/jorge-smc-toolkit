"""Tests for tools/nandcheck.py using small synthetic dumps.

Run from the repo root:  python -m unittest discover -s tests
"""

import io
import os
import struct
import sys
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
import nandcheck  # noqa: E402

SMC_OFFSET = 0x1000
SMC_PLAIN = bytes((i * 7 + 3) & 0xFF for i in range(0x3000))


def make_logical(size=0x1000000):
    """A blank 16MB image with a plausible flash header and an encrypted SMC."""
    data = bytearray(b"\xff" * size)
    hdr = bytearray(0x80)
    struct.pack_into(">HH", hdr, 0x00, 0xFF4F, 1888)
    struct.pack_into(">I", hdr, 0x08, 0x8000)
    notice = b"\xa9 2004-2011 Microsoft Corporation. All rights reserved."
    hdr[0x10:0x10 + len(notice)] = notice
    struct.pack_into(">I", hdr, 0x6C, 0x4000)
    struct.pack_into(">II", hdr, 0x78, len(SMC_PLAIN), SMC_OFFSET)
    data[0:0x80] = hdr
    data[SMC_OFFSET:SMC_OFFSET + len(SMC_PLAIN)] = nandcheck.smc_encrypt(SMC_PLAIN)
    return bytes(data)


def add_ecc(logical):
    spare = b"\x00" * nandcheck.SPARE
    return b"".join(logical[i:i + nandcheck.PAGE] + spare
                    for i in range(0, len(logical), nandcheck.PAGE))


class NandcheckTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def write(self, name, data):
        path = os.path.join(self.tmp.name, name)
        with open(path, "wb") as f:
            f.write(data)
        return path

    def run_cli(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = nandcheck.main(list(argv))
        return code, out.getvalue() + err.getvalue()

    def test_smc_round_trip(self):
        enc = nandcheck.smc_encrypt(SMC_PLAIN)
        self.assertNotEqual(enc, SMC_PLAIN)
        self.assertEqual(nandcheck.smc_decrypt(enc), SMC_PLAIN)

    def test_strip_ecc_restores_logical_image(self):
        logical = make_logical()
        raw = add_ecc(logical)
        self.assertEqual(len(raw), 0x1080000)
        self.assertEqual(nandcheck.strip_ecc(raw), logical)

    def test_info_accepts_good_dump_with_ecc(self):
        path = self.write("good.bin", add_ecc(make_logical()))
        code, out = self.run_cli("info", path)
        self.assertEqual(code, 0, out)
        self.assertIn("ECC:      present", out)
        self.assertIn("SMC at:   0x1000, 0x3000 bytes", out)

    def test_info_accepts_good_dump_without_ecc(self):
        path = self.write("good.bin", make_logical())
        code, out = self.run_cli("info", path)
        self.assertEqual(code, 0, out)
        self.assertIn("ECC:      not present", out)

    def test_info_flags_blank_dump(self):
        path = self.write("blank.bin", b"\x00" * 0x1080000)
        code, out = self.run_cli("info", path)
        self.assertEqual(code, 1)
        self.assertIn("first page is blank", out)

    def test_info_flags_truncated_dump(self):
        path = self.write("short.bin", add_ecc(make_logical())[:0x800000])
        code, out = self.run_cli("info", path)
        self.assertEqual(code, 1)
        self.assertIn("doesn't match any known dump size", out)

    def test_compare_identical(self):
        raw = add_ecc(make_logical())
        a, b = self.write("a.bin", raw), self.write("b.bin", raw)
        code, out = self.run_cli("compare", a, b)
        self.assertEqual(code, 0, out)
        self.assertIn("identical", out)

    def test_compare_reports_mismatched_block(self):
        raw = bytearray(add_ecc(make_logical()))
        a = self.write("a.bin", bytes(raw))
        block = nandcheck.BLOCK_PAGES * nandcheck.RAW_PAGE
        raw[5 * block + 10] ^= 0xFF
        b = self.write("b.bin", bytes(raw))
        code, out = self.run_cli("compare", a, b)
        self.assertEqual(code, 1)
        self.assertIn("MISMATCH in 1 block(s)", out)
        self.assertIn("0x5", out)

    def test_compare_different_sizes(self):
        a = self.write("a.bin", make_logical())
        b = self.write("b.bin", add_ecc(make_logical()))
        code, out = self.run_cli("compare", a, b)
        self.assertEqual(code, 1)
        self.assertIn("different sizes", out)

    def test_smc_command_writes_decrypted_smc(self):
        path = self.write("good.bin", add_ecc(make_logical()))
        out_path = os.path.join(self.tmp.name, "smc.bin")
        code, out = self.run_cli("smc", path, out_path)
        self.assertEqual(code, 0, out)
        with open(out_path, "rb") as f:
            self.assertEqual(f.read(), SMC_PLAIN)

    def test_strip_ecc_command(self):
        logical = make_logical()
        path = self.write("good.bin", add_ecc(logical))
        out_path = os.path.join(self.tmp.name, "noecc.bin")
        code, out = self.run_cli("strip-ecc", path, out_path)
        self.assertEqual(code, 0, out)
        with open(out_path, "rb") as f:
            self.assertEqual(f.read(), logical)


if __name__ == "__main__":
    unittest.main()
