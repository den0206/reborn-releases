<p align="center">
  <img src="assets/icon.png" alt="Reborn icon" width="128" height="128">
</p>

<h1 align="center">Reborn</h1>

<p align="center">
  <strong>Save your window arrangement. Get it back with one click.</strong><br>
  A minimal macOS menu bar app built for multi-monitor setups.
</p>

<p align="center">
  <a href="https://github.com/den0206/reborn-releases/releases/latest"><img alt="Download DMG" src="https://img.shields.io/badge/Download-Reborn.dmg-2f7bff?style=for-the-badge&labelColor=111111"></a>
</p>

<p align="center">
  <!-- BEGIN:release-badge -->
  <a href="https://github.com/den0206/reborn-releases/releases/latest"><img alt="Latest release" src="https://img.shields.io/badge/Release-Ver__0.0.3%2B1-2f7bff?style=flat-square&labelColor=111111"></a>
  <!-- END:release-badge -->
  <img alt="macOS 26+" src="https://img.shields.io/badge/macOS-26%2B-2f7bff?style=flat-square&labelColor=111111">
  <img alt="Universal Binary" src="https://img.shields.io/badge/Universal-Apple%20Silicon%20%2F%20Intel-2f7bff?style=flat-square&labelColor=111111">
  <img alt="Swift 6" src="https://img.shields.io/badge/Swift-6-2f7bff?style=flat-square&labelColor=111111">
  <img alt="Free" src="https://img.shields.io/badge/Price-Free-2f7bff?style=flat-square&labelColor=111111">
  <img alt="No tracking" src="https://img.shields.io/badge/Tracking-None-2f7bff?style=flat-square&labelColor=111111">
</p>

<p align="center">
  English · <a href="README.ja.md">日本語</a>
</p>

<!-- BEGIN:latest-release -->
<p align="center">
  Latest release: <strong>0.0.3+1</strong> (released 2026-08-08)
</p>
<!-- END:latest-release -->

---

**Reborn** is a macOS menu bar app that saves the position, size, and monitor assignment of your
open application windows, then restores them with a single click.

> "Put the MacBook back on the desk, and the workspace is already the way you left it."

Unplug the external displays, take the laptop out, come back and plug them in again — instead of
dragging every window back into place, you get it done from the menu bar in **one click**
(or automatically, just by connecting the display).

**Reborn is completely free.** Every feature is available to everyone — there is no paid tier,
no subscription, no in-app purchase, no trial period, and no feature that is unlocked by paying.
There are no ads and no telemetry, and no account is required.
It makes network requests only when you press "Check for Updates" or "Update".

This repository hosts the **distributed releases (DMG)**. The application source code lives in a separate repository.

## Contents

- [What It Does](#what-it-does)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Feature Overview](#feature-overview)
- [Settings](#settings)
- [How Multi-Monitor Works](#how-multi-monitor-works)
- [Updating](#updating)
- [Uninstall](#uninstall)
- [Pricing](#pricing)
- [Privacy and Security](#privacy-and-security)
- [Limitations](#limitations)
- [Troubleshooting](#troubleshooting)
- [Versioning](#versioning)

## What It Does

- **Save an arrangement** — captures the position, size, and monitor of every open window under a name you choose. Minimized windows are included.
- **Restore in one click** — click a name in the menu bar list and your windows move back.
- **Auto restore** — detects display changes and applies the layout matching the new configuration (off by default).
- **Global shortcuts** — assign a key combination (for example ⌃⌥⌘1) per layout and trigger it from anywhere.
- **Multi-monitor aware** — displays are identified by UUID, so layouts survive reconnection order and resolution changes.
- **Layout preview** — a minimap in the settings window shows what a saved layout actually looks like.
- **Clean restore** — pick the same layout again and, after confirmation, apps outside the layout are quit before rearranging (off by default).
- **App exclusions / privacy mode** — leave specific apps alone, or stop saving window titles entirely.
- **Export / import** — move layouts around as `.rebornlayout` files.

There is no Dock icon. Reborn never polls while idle; it is designed for 0% idle CPU.

## Quick Start

### Requirements

| Item | Value |
|------|-------|
| OS | **macOS 26 Tahoe or later** |
| Architecture | Apple Silicon / Intel (Universal Binary) |
| Permissions | Accessibility (required) / Notifications (optional) |
| Dependencies | None (zero third-party libraries) |

### Install

1. Download `Reborn-X.Y.Z.dmg` from [**Releases**](https://github.com/den0206/reborn-releases/releases/latest).
2. Open the DMG and **drag `Reborn.app` into your `Applications` folder**.
3. Launch Reborn from `Applications`.

> **Do not run Reborn directly from the DMG.**
> Launching from a mounted disk image or an external drive registers that path with macOS, leaving a
> separate row per release under Login Items and "Allow in the Menu Bar" — and in-app updates will not work.
> Reborn detects this at launch and offers to move itself into `Applications`.

### First Launch

An onboarding window appears and asks for **Accessibility permission**.

macOS requires this permission for any app that moves or resizes another app's windows.
Grant it under "System Settings > Privacy & Security > Accessibility" and onboarding advances automatically.

Reborn reads only **window position, size, title, and minimized state**.
It never touches window contents or keyboard input.

> **If Gatekeeper warns you**
> Release DMGs are signed with a Developer ID and notarized by Apple.
> If you still see "cannot verify the developer", right-click `Reborn.app` → "Open" once to allow it.

## Usage

Click the ⧉ icon (`macwindow.on.rectangle`) in the menu bar to open the popover.

### Save an arrangement

1. Arrange your windows the way you want them.
2. Menu bar icon → "**＋ Save Current Layout**".
3. A preview of the apps being saved appears inline. Type a name and press **Enter**.

The default name is derived from the display configuration and date (for example "2 Monitors 2026-07-25").
If the name already exists, a number is appended to make it unique ("Work" → "Work 2").

### Restore an arrangement

**Just click the row.** A spinner shows while it runs, then a ✓ appears for one second.

Restore is **best-effort**: if one window cannot be placed, the rest still proceed, and you get a
summary such as "Placed 12 windows (2 skipped)".

### Manage layouts

| Action | How |
|--------|-----|
| Update with current layout | Right-click the row → "Update with Current" (name and shortcut are preserved) |
| Rename | Right-click the row → "Rename", or edit inline under Settings > Layouts |
| Delete | Right-click the row → "Delete". Hold ⌘ to skip the confirmation |
| Reorder | Drag and drop under Settings > Layouts |
| Import | Drag a `.rebornlayout` file onto the popover |

### Keyboard

| Key | Action |
|-----|--------|
| `↑` `↓` | Select a row |
| `Enter` | Restore the selected layout |
| `⌘⌫` | Delete the selected layout |
| `⌘,` | Open Settings |
| `Esc` | Close the popover |

### Reading a row

- The 🖥 badges on the left show **how many displays** were connected when the layout was saved.
- Layouts matching your current configuration get a tinted badge — those are ready to use right now.
- Rows whose display count differs from now are **greyed out with a ⚠️** and cannot be clicked.
  The tooltip explains why: "Saved with 2 displays / currently 1".

## Feature Overview

| Feature | Description |
|---------|-------------|
| Save layout | Stores position, size, monitor assignment, and minimized state of all windows under a name (up to 20 layouts) |
| Restore layout | Applies a saved arrangement — by click, shortcut, or automatically |
| Layout management | List, rename, update in place, delete, reorder |
| Multi-monitor support | Displays identified by UUID; remapped by relative coordinates when the configuration changes |
| Permission onboarding | Explains why Accessibility is needed and links straight to System Settings |
| Auto restore | Detects display configuration changes and applies the matching layout (off by default) |
| Global shortcuts | Per-layout key assignment; at least one modifier key is required |
| Open at login | Registers a login item via `SMAppService` |
| Notifications & sound | Restore summary notifications plus a discreet success sound (toggleable) |
| Export / import | Exchange layouts as `.rebornlayout` (JSON) files |
| App exclusions | Keep specific apps out of both save and restore |
| Privacy mode | Do not store window titles |
| Display count guard | Refuses to restore when the display count differs from save time (always on) |
| Layout preview | Minimap of a saved layout in the settings window |
| Update check | Checks for a newer release once, only when you press the button |
| In-app update | Downloads, verifies, and swaps in the new build with progress shown |
| Clean restore | Re-selecting the same layout quits apps outside it, then rearranges (off by default) |
| Install location guard | Prompts to move into `Applications` when running from a DMG or external drive |
| Uninstall | Unregisters the login item, trashes the app, and removes stored data in one step |

## Settings

Open with the ⚙ button in the popover or `⌘,`. There are three tabs.

### General

**Launch & Notifications**

- **Launch at Login** — start Reborn when your Mac starts.
- **Show Notifications** — post restore summaries to Notification Center.
- **Play Sound on Success** — a discreet system sound after a successful save or restore (on by default).

**Restore**

- **Auto-Restore When Display Arrangement Changes** — applies the layout matching the new
  configuration (off by default). If several layouts match, the first one in the list wins. Suppressed if
  you restored manually within the last 30 seconds.
- **Launch Apps That Aren't Running** — starts apps that were open at save time but are closed now, then places their windows.
- **Quit apps outside the layout when reselecting it** — enables clean restore (off by default).

**Privacy**

- **Don't Save Window Titles** — titles are not stored and windows are matched by order only, which is less precise.
  Turning this on also erases titles already stored in existing layouts.

**Apps to Ignore**

- Pick from the running-apps menu to exclude an app from both save and restore.

### Layouts

- The layout list (drag to reorder). Each row shows the name, a summary of the apps it contains, a shortcut
  recorder field, and a delete button.
- Layouts matching your current display configuration are marked with a "Current setup" pill.
- Selecting a row reveals a **layout preview** (minimap) below, plus chips for every app included.
  The divider between the list and the preview can be dragged to resize.
- Buttons at the bottom **export and import** layouts.

**Assigning a shortcut**: click the recorder field (it reads "None" when unassigned) and press the key combination.
Combinations without a modifier key are rejected. If the key is already assigned to another layout,
a warning appears and you confirm before overwriting.

### About

- App name and version
- Privacy statement
- **Check for Updates** button (followed by "Update" / "Open Release Page" depending on the result)
- Accessibility permission status, with a button to open System Settings
- **Uninstall Reborn…**

## How Multi-Monitor Works

This is the part Reborn cares most about.

### Identifying displays

The order of `NSScreen` and `CGDirectDisplayID` values change between connections, so they are never used
as identifiers. Reborn identifies each display by its **UUID**.

### When the configuration changes

| Situation | Behavior |
|-----------|----------|
| Same configuration as save time | The saved coordinates are applied as-is |
| Same display count, different displays | Windows are re-placed using **relative coordinates (normalized 0–1)** within each display, preserving proportions across resolutions |
| A display from save time is gone | Windows move to the main display, keeping their relative position within the original display |
| **The display count itself differs** | **No restore is performed** (display count guard). The row is greyed out; shortcut triggers explain the reason via notification |

After placement, windows are clamped into the visible area (at least 100×100pt always stays on screen).
That is why **restoring with a display unplugged never sends windows off-screen**.

### Matching windows

Saved records are matched against current windows, per app, in this order:

1. Exact window title match
2. Title prefix match (handles changes like `Document — Edited`)
3. The window's order at save time
4. **If nothing matches, the window is left alone**

Doing nothing is always preferred over moving the wrong window.

## Updating

Reborn fetches public release information exactly once, and only when you press
Settings > "About" → "**Check for Updates**". There is no launch-time or background check.

When a newer version is found:

- **Update** — downloads the DMG in-app, verifies the code signature, notarization, and Team ID, then replaces
  itself and relaunches. Shown only for release builds installed in a writable location.
  On failure your existing installation is left untouched, temporary files are fully removed, and you are
  handed the release page link instead.
- **Open Release Page** — for downloading manually.

Network access is restricted to `github.com` and `*.githubusercontent.com`.

## Uninstall

A macOS app cannot detect that it has been dragged to the Trash. So simply trashing `Reborn.app`
**leaves the login item registration and your stored data behind as orphans**.

Use Settings > "About" → "**Uninstall Reborn…**" instead. It performs the cleanup in the right order:

1. Unregisters the login item
2. Moves `Reborn.app` to the Trash
3. Deletes stored data (settings and layouts)
4. Quits

> **Accessibility permission cannot be removed by the app** — macOS provides no API for it.
> Remove the Reborn entry manually under "System Settings > Privacy & Security > Accessibility".

If you want to clean up by hand, the data lives at:

```
~/Library/Application Support/Reborn
```

## Pricing

**Reborn is free. All of it.**

| | |
|---|---|
| Price | Free |
| Paid tier / Pro version | None — there is only one version, and it has every feature |
| Subscription | None |
| In-app purchase | None |
| Trial period or usage limit | None |
| Ads | None |
| Account / sign-up | Not required |

Every release published here is the complete app. Nothing is held back for a paid edition, and there
is no plan to gate existing features behind a payment later.

## Privacy and Security

- **All data stays on your Mac.** No cloud sync, no account.
- **Only window position, size, title, and minimized state are collected.** Window contents and keyboard input are never accessed.
- **Network requests happen only when you explicitly press a button**: "Check for Updates" (one metadata
  fetch) and "Update" (the DMG download). Both are restricted to `github.com` / `*.githubusercontent.com`.
  There is no tracking, analytics, or crash reporting of any kind.
- **Zero third-party libraries.** Everything is built on public macOS APIs.
- No private APIs. Other apps' windows are manipulated through the **public Accessibility API** only.
- Releases ship with **Hardened Runtime enabled, Developer ID signing, and Apple notarization** (both the `.app` and the DMG are signed and stapled).
- App Sandbox is not used — it is incompatible with the Accessibility API needed to control other apps.
  This is also why Reborn cannot be distributed on the Mac App Store.
- Stored files (settings and layouts) are written with `0600` permissions.
- **The only feature that quits other apps is clean restore**, and only after you enable the setting and
  approve the inline confirmation. It sends a normal Quit — never a force quit — so apps with unsaved
  changes are not terminated. Finder, Dock, System Settings and similar are on a protected list.

See [PRIVACY.md](PRIVACY.md) for details.

## Limitations

Things Reborn **deliberately does not do**, plus its current constraints.

- **No window tiling or snapping.** That would conflict with the built-in macOS features and with tools like Rectangle.
- **No moving windows between Spaces.** It would require private APIs.
- **Full-screen windows are not touched.** They are recorded but skipped on restore. The same applies to Stage Manager.
- **Some apps cannot be controlled.** Certain Electron- and Java-based apps do not respond to the Accessibility API.
  Those windows are skipped and reported in the restore summary.
- **Not available on the Mac App Store** (App Sandbox is incompatible). Distribution is by DMG only.
- Up to **20 layouts** can be saved (by design — Reborn stays minimal).
- Clean restore does not combine with shortcuts. Shortcut and auto-restore paths cannot show a confirmation
  UI, so they always perform a normal restore.

## Troubleshooting

### A layout row is greyed out and won't respond

The **number of displays** currently connected differs from when that layout was saved (display count guard).
The tooltip shows "Saved with 2 displays / currently 1". Reconnect the display, or save a new layout for
your current setup.

### Only some windows get restored

One of the following. The restore summary reports the skipped count.

- The app is not running → enable Settings > "Launch Apps That Aren't Running"
- There are fewer windows now than at save time → open the missing windows first
- The window is full-screen or managed by Stage Manager → out of scope by design
- The app does not respond to the Accessibility API (some Electron/Java apps) → no workaround at present
- The app is on your exclusion list → check Settings > "Apps to Ignore"

### The menu bar icon shows ⚠️

Accessibility permission was lost. This can happen after a macOS update or a reinstall.
Use the banner at the top of the popover, or Settings > "About" → "Open System Settings", and re-authorize Reborn.

If toggling the checkbox off and on does not help, reset the registration in Terminal and relaunch:

```bash
tccutil reset Accessibility com.yuukisakai.reborn
```

### System Settings lists Reborn several times

If you ever launched Reborn from a DMG or an external drive, macOS registered **each path** separately.
Keep only the entry for the copy in your `Applications` folder and remove the rest, then always launch
from `Applications`.

### A shortcut does not fire

- Include at least one modifier key (⌘ / ⌃ / ⌥ / ⇧). Bare keys cannot be registered.
- Check for conflicts with another app or a system shortcut — whichever process registered the combination
  first wins.

### In-app update fails

Reborn must be installed in a **writable location** such as `Applications`.
In-app updates are unavailable when running from a DMG. Even on failure your installation is left unchanged,
so just download the new version manually from the release page.

### Restored windows are slightly off

Some apps adjust the position or size they were given. Reborn reads the actual frame back after applying it
and retries once if the difference exceeds 5pt, but a few stubborn apps still win.

## Versioning

Tags use the `Ver_X.Y.Z` form. A rebuild of the same `X.Y.Z` is tagged `Ver_X.Y.Z+N`
(for example `Ver_0.0.1+1`), and the in-app update check treats `X.Y.Z+N` as newer than `X.Y.Z`.

See [CHANGELOG.md](CHANGELOG.md) for the release history.

## Links

| | |
|---|---|
| Download | [Releases](https://github.com/den0206/reborn-releases/releases/latest) |
| Changelog | [CHANGELOG.md](CHANGELOG.md) |
| Privacy | [PRIVACY.md](PRIVACY.md) |
| Bugs & requests | [Issues](https://github.com/den0206/reborn-releases/issues) |

---

The source code is kept in a private repository. This repository exists solely to publish the distributed releases.
