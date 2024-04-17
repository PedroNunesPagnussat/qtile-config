#!/usr/bin/env bash

find ~/Pictures/wallpaper/ -type f | shuf -n 1 | xargs xwallpaper --stretch &

