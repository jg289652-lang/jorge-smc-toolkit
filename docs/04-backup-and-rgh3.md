# 4. Backups and permanent RGH3 (optional)

The softmod has to be re-run after every power-on. **RGH 3.0** makes the mod
permanent: you solder two wires and flash a modified NAND image, and the
console boots straight into Aurora every time. Unlike older RGH versions, it
needs no glitch chip. It reprograms the console's own SMC, the small
controller that handles power-on, to do the glitching.

**Not possible on Winchester boards** (see [step 1](01-identify-your-console.md)).

This step can brick the console if it goes wrong. If you haven't soldered
fine-pitch wires before, practise on scrap electronics first or pay a modder.

## Step A: back up the NAND and CPU key

The NAND is the console's flash chip. It holds the bootloaders, the SMC
firmware, and the keyvault, which is unique to your console and can't be
replaced. The **CPU key** is a per-console key burned into the CPU; you need
it to decrypt the NAND and build a hacked image.

With the softmod running, you can dump both in software, with no NAND reader
and no soldering. The ConsoleMods page
[Dumping your NAND and CPU Key](https://consolemods.org/wiki/Xbox_360:Dumping_your_NAND_and_CPU_Key)
has the current method.

1. Dump the NAND **at least twice**.
2. Check the dumps:

   ```
   python tools/nandcheck.py info nanddump1.bin
   python tools/nandcheck.py compare nanddump1.bin nanddump2.bin
   ```

   Both must pass. If `compare` reports a mismatch, dump again. Don't build
   anything from dumps that disagree.
3. Save the dumps and the CPU key (a 32-character hex string) in at least two
   places, such as your PC and a cloud drive. Name the folder after the
   console's serial number.

If dumps from a 4GB model (MMC/eMMC flash) disagree, take them back to back
without using the console in between, then compare again. Don't use dumps
that still disagree.

## Step B: get a NAND flasher before you flash

ConsoleMods strongly recommends having a hardware NAND flasher before you
write a modified image, because it's the only way to recover if the new image
doesn't boot. **PicoFlasher** (a Raspberry Pi Pico, a few dollars) is the
usual choice. 4GB Corona boards need a PicoFlasher variant or an SD-card-based
reader that supports MMC.

## Step C: build the image

Use **J-Runner with Extras** (Windows). Load your dump and CPU key, then
select **Glitch2** as the image type; that's the option RGH3 uses. J-Runner
builds the modified image and writes the RGH3 SMC for your board type.

## Step D: wire RGH3 and flash

Follow the [ConsoleMods RGH3 guide](https://consolemods.org/wiki/Xbox_360:RGH/RGH3)
for your exact board. The short version:

- Two wires run between points on the motherboard, with one resistor.
  ConsoleMods lists 3K for Trinity and 1K for Corona.
- Later Corona revisions need a POST fix adapter.
- Flash the image, power on, and the console should boot to Aurora.
  Slow or inconsistent boots usually come down to the wire routing or the
  resistor value. The guide covers tuning.

## Keep this

Once it works, keep your original dumps forever. They're the only way to
return the console to stock or rebuild the image after a future change.
