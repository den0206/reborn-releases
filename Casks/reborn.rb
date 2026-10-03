# Generated file — do not edit by hand.
# Source: Scripts/homebrew-cask.sh in the Reborn source repository, run by its release workflow.
cask "reborn" do
  version "0.1.0"
  sha256 "272fd8d05386b4d99c02c03144b0171ff83a3f4f459c4b813c891001b13447cd"

  url "https://github.com/den0206/reborn-releases/releases/download/Ver_#{version}/Reborn-#{version}.dmg",
      verified: "github.com/den0206/reborn-releases/"
  name "Reborn"
  desc "Menu bar app that saves and restores window layouts across multiple displays"
  homepage "https://github.com/den0206/reborn-releases"

  livecheck do
    url :url
    strategy :github_latest
    regex(/^Ver[._-]?v?(\d+(?:\.\d+)+(?:\+\d+)?)$/i)
  end

  # Reborn updates itself (Settings > About > "Check for Updates" > "Update"), so brew
  # must not fight it: without this stanza every `brew upgrade` would reinstall the app.
  auto_updates true
  depends_on macos: ">= :tahoe"

  app "Reborn.app"

  uninstall quit: "com.yuukisakai.reborn"

  zap trash: [
    "~/Library/Application Support/Reborn",
    "~/Library/Caches/com.yuukisakai.reborn",
    "~/Library/HTTPStorages/com.yuukisakai.reborn",
    "~/Library/Preferences/com.yuukisakai.reborn.plist",
  ]

  caveats <<~CAVEATS
    Reborn needs Accessibility permission to move other applications' windows.
    Grant it in System Settings > Privacy & Security > Accessibility on first launch.

    Reborn can update itself, so `brew upgrade` leaves it alone by design.
    Use the in-app updater, or `brew upgrade --cask --greedy reborn`.

    `brew uninstall` cannot unregister the login item (macOS offers no API for that).
    To remove everything, use the in-app uninstaller first
    (Settings > About > "Uninstall Reborn…"), or turn Reborn off under
    System Settings > General > Login Items after uninstalling.
  CAVEATS
end
