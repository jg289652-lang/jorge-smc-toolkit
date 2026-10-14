# 2. Softmod with ABadAvatar

ABadAvatar is a software-only exploit. A crafted avatar file on a USB stick
breaks the console's security when the dashboard loads it. Then a payload
takes over and lets you run unsigned code. Nothing on the console is changed
permanently: if you power off, the console is back to stock.

## What you need

- The console on dashboard 17559 ([step 1](01-identify-your-console.md)).
- A USB stick. Smaller, older ones work best: 8–32GB, USB 2.0 if you have
  one. Some USB 3.0 sticks fail. It gets wiped.
- A PC. Windows is easiest, because BadBuilder can format the stick there. On
  Mac or Linux, format the stick yourself as **FAT32** (not exFAT, not NTFS)
  first.

## Build the USB stick

Use **[BadBuilder](https://github.com/Pdawg-bytes/BadBuilder)**. It formats
the stick, downloads the exploit and payload files, and puts them in the
right folders. It needs the .NET 8 runtime.

1. Download the latest BadBuilder release and run it.
2. Select your USB stick.
3. Choose **ABadAvatar** as the exploit.
4. Choose a payload:
   - **XeUnshackle** (recommended). The full option: it includes DashLaunch
     with plugin support, and it can auto-launch a dashboard. You need it for
     mod-menu plugins.
   - **FreeMyXe**. Lighter. Fine for plain homebrew and XeLL, but no plugin
     loader.
5. When it offers to add homebrew, add **Aurora** (download the latest Aurora
   zip first). This is the dashboard you'll use for everything else.

## Run the exploit

1. **Go offline.** Unplug the Ethernet cable. In **Settings → System →
   Network Settings**, forget the wireless network.
2. **Turn off auto sign-in** on your profile so the console stops at the
   profile-select screen.
3. With the console off, plug in the USB stick, then power on.
4. Open the sign-in / profile-select screen. The exploit profile on the USB
   loads its avatar, and the avatar triggers the exploit. **Don't sign in to
   the exploit profile.** Its README is especially clear about never doing it
   while connected to Xbox Live.
5. When the exploit works, the payload's screen appears. XeUnshackle can then
   take you to Aurora.

It doesn't work every time; guides put the success rate at about 80%. If the
console freezes or nothing happens, hold the power button to turn it off and
try again.

**Every time you power on**, repeat steps 3–5. Leave the stick plugged in.
Newer ABadAvatar builds (1.3 and later) can boot more directly into the
modded state. Check the release notes for the current options.

## If it isn't working

- Check the kernel is exactly 17559.
- Try a different, older USB stick, and make sure it's FAT32.
- Make sure the avatar data is installed (see step 1).
- Read the issues page on the ABadAvatar and BadBuilder GitHub repos. Most
  problems are already answered there.

Next: [3. Homebrew, trainers and mod menus](03-homebrew-and-mods.md)
