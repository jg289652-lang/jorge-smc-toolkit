# 1. Identify your console

## Which model is it?

| | Xbox 360 S (2010–2013) | Xbox 360 E (2013–2016) |
|---|---|---|
| Look | Black, curved top and sides, glossy or matte | Two-tone black and grey, flat and boxy, looks like an Xbox One |
| Power / eject | Touch-sensitive (no click) | Physical buttons that click |
| Motherboard | Trinity, or Corona on later units | Corona, or Winchester on late units |

**For the softmod in step 2, the model doesn't matter.** ABadAvatar works on
all of them. The motherboard only matters if you later want permanent RGH3.

## Check the dashboard version

ABadAvatar needs dashboard **17559**, the last update Microsoft released.

1. Go to **Settings → System → Console Info**.
2. Look at the **Kernel** line. It should end in `17559`.

If it shows a lower number, update before you mod anything. The console is
still stock at this point, so updating over the internet is safe. The other
option is Microsoft's offline USB system update.

Also look at your avatar on the home screen. If avatars appear grey or
missing, install the system update anyway. The exploit loads through avatar
data, so it needs that data installed.

## Find your motherboard (only needed for RGH3)

Use **Octal's Identification Wizard**, which the
[ConsoleMods Getting Started page](https://consolemods.org/wiki/Xbox_360:Getting_Started)
links to and recommends. You enter what you see (the console model, the
amperage on the label on the back of the console, the manufacture date) and
it tells you the board.

What the answer means for you:

- **Trinity:** RGH3 works.
- **Corona:** RGH3 works. Check whether it's a 4GB model (internal storage, no
  hard drive). Those use MMC flash, which needs different tools to back up.
  Later Corona revisions can also need a small "POST fix" adapter.
- **Winchester:** RGH and JTAG are impossible on this board. Stick with the
  softmod. It still gives you Aurora, trainers and plugins; you just re-run it
  after each power-on.

Write down your model, kernel version and board. You'll need them later.
