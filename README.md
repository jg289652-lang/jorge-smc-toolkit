# jorge-smc-toolkit

Notes and tools for modding my Xbox 360 S/E so it can run homebrew, a custom
dashboard, trainers and offline mod menus.

## The plan

1. **Softmod first ([guide](docs/02-softmod.md)).** ABadAvatar is a
   software-only exploit: a USB stick, no opening the console, no soldering.
   It works on every 360 model, including the late "Winchester" boards that
   can't be hardware-modded. The catch is that it doesn't survive a reboot,
   so you re-run it each time you power on.
2. **Play ([guide](docs/03-homebrew-and-mods.md)).** Aurora dashboard,
   trainers (cheat menus for single-player), and mod-menu plugins, all offline.
3. **Optional: make it permanent ([guide](docs/04-backup-and-rgh3.md)).**
   RGH 3.0 is a two-wire solder mod that boots straight into the modded
   dashboard every time. Only do this after the softmod works and you have a
   verified NAND backup.

Start with **[docs/01-identify-your-console.md](docs/01-identify-your-console.md)**
to check which console you have and get it on the right dashboard version.

## Ground rules

- **Stay off Xbox Live while modded.** Microsoft bans modded consoles, and a
  console ban is permanent. Unplug Ethernet and forget the Wi-Fi network
  before you run the exploit.
- **Back up before any hardware change.** The NAND dump is your only undo
  button. Dump it more than once and check the copies with `tools/nandcheck.py`.
- **Use games you own.** Everything here works with your own discs and
  digital purchases.
- **Exact menus and file names change between releases.** These docs give
  the order of steps and the reasons for them. For the exact clicks, follow
  the README of the current release of each tool, and the ConsoleMods wiki.

## Tools

`tools/nandcheck.py` checks NAND dumps before you rely on them. It needs
Python 3.8 or newer and nothing else.

```
python tools/nandcheck.py info nanddump1.bin
python tools/nandcheck.py compare nanddump1.bin nanddump2.bin
python tools/nandcheck.py strip-ecc nanddump1.bin nanddump1_noecc.bin
python tools/nandcheck.py smc nanddump1.bin smc_decrypted.bin
```

- `info` names the dump layout from its size, reads the flash header, and
  flags obvious corruption: a blank first page, a wrong size, a bad header.
- `compare` checks that two or more dumps are byte-identical and lists any
  blocks that differ.
- `strip-ecc` removes the 16 spare bytes after each 512-byte page.
- `smc` extracts the SMC (the console's power and boot controller firmware)
  and decrypts it, so you can look at what RGH3 patches.

Run the tests with `python -m unittest discover -s tests`.

## Sources

- ConsoleMods wiki: [Bad Update](https://consolemods.org/wiki/Xbox_360:Bad_Update),
  [Exploit Chart](https://consolemods.org/wiki/Xbox_360:Exploit_Chart),
  [Getting Started](https://consolemods.org/wiki/Xbox_360:Getting_Started),
  [RGH3](https://consolemods.org/wiki/Xbox_360:RGH/RGH3),
  [Dumping your NAND and CPU Key](https://consolemods.org/wiki/Xbox_360:Dumping_your_NAND_and_CPU_Key)
- [ABadAvatar](https://github.com/shutterbug2000/ABadAvatar) (the exploit)
- [BadBuilder](https://github.com/Pdawg-bytes/BadBuilder) (builds the USB stick)
- Free60 wiki: [NAND file system](https://free60.org/System-Software/NAND_File_System/),
  [SMC hack](https://free60.org/Hacks/SMC_Hack/)
