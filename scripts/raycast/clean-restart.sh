#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Clean Restart
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.author andboyxd
# @raycast.authorURL https://raycast.com/andboyxd

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
echo "$SECRET" | sudo -S -k shutdown -r now
