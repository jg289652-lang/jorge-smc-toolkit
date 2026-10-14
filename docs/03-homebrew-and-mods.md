# 3. Homebrew, trainers and mod menus

Everything here assumes the exploit from [step 2](02-softmod.md) is running
and the console is offline.

## Aurora: your new dashboard

Aurora replaces the Microsoft dashboard with a game library that launches
anything: your installed games, homebrew apps, emulators.

- Add the drives you keep games on (internal HDD, USB drive) as scan paths,
  and Aurora builds the library with box art.
- Aurora has a file manager, so you can copy files between USB and the
  internal drive without a PC.
- Your own disc games keep working as normal.

## Trainers: cheat menus with no coding

Trainers are the easiest way to get the "admin menu" feel in single-player
games: infinite health or ammo, unlimited money, unlocking items. Aurora has
built-in trainer support. Community trainer packs list which games and which
title-update version they support. You enable a trainer in Aurora before
launching the game, then toggle cheats in-game with a button combo. The
trainer's description tells you which combo.

Trainers patch memory for one exact game version. If a trainer does nothing,
check that the game's title update matches what the trainer says it needs.

## Mod menus: plugins

Bigger mod menus (the ones with in-game menus, spawning, teleporting, and so
on) are **plugins**: `.xex` files that load alongside the game and patch it
while it runs. DashLaunch, which XeUnshackle includes, loads them.

DashLaunch reads its settings from a file called `launch.ini`. The parts you
care about look like this:

```ini
[Plugins]
plugin1 = Usb:\Plugins\SomeMenu.xex

[Settings]
liveblock = true
```

- `plugin1`…`plugin5` are the plugin slots. Point one at the menu's `.xex`.
- `liveblock = true` blocks connections to Xbox Live servers. Keep it on.

DashLaunch ships with a commented example `launch.ini`; start from that one
rather than writing it from scratch. The path format (`Usb:\`, `Hdd:\`)
depends on where you put the file.

Rules of thumb for menus:

- Use menus offline, in single-player, or in System Link with your own
  consoles. Many menus are built for online lobbies; don't take them there.
- Like trainers, menus target one specific title update of the game.
- Get them from well-known community sources. They're executable code, so
  treat a menu from an unknown uploader like any other untrusted program.
- If the console freezes on game launch, remove the plugin line and try one
  plugin at a time.

## Writing your own code

There are two different routes, and they need different toolchains.

**Homebrew apps on bare hardware (open source).** LibXenon is Free60's open
toolchain for writing C programs that run directly on the 360's hardware.
FreeMyXe can launch XeLL, the bootloader these programs start from. It's a
good way to learn how the hardware works, but these programs run instead of
the Xbox OS, not alongside games.

**Plugins and game mods (what mod menus are).** These are C++ DLL-style `.xex`
modules. They hook a game's functions or patch its memory at addresses found
by reverse-engineering the game's executable (Ghidra works for this).
Building them normally needs Microsoft's Xbox 360 SDK (the XDK), which isn't
publicly licensed, so you'd have to source that yourself.

Once your console runs plugins, a good first project is a tiny plugin that
shows an on-screen notification when a game launches. It proves your build
and load setup works before you start on a real menu.

Next: [4. Backups and permanent RGH3](04-backup-and-rgh3.md) (optional)
