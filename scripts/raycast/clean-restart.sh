#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Clean Restart
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "password" }
# @raycast.needsConfirmation true

osascript -e 'quit app "Mail"'
osascript -e 'quit app "Calendar"'
osascript -e 'quit app "BetterZip"'
osascript -e 'quit app "Discord"'
osascript -e 'quit app "Obsidian"'
osascript -e 'quit app "Obsidian"'
osascript -e 'quit app "Visual Studio Code"'
osascript -e 'quit app "Spotify"'
osascript -e 'quit app "iTerm"'
pkill -x Transmission

source ~/.bashrc
echo "$1" | sudo -S -k shutdown -r now
