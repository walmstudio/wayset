#!/bin/bash

echo "Stopping Wayset"

sudo systemctl stop wayset

echo "Uninstalling Wayset"

sudo rm /usr/local/bin/wayset
sudo rm -r /usr/share/wayset
sudo rm /usr/share/icons/wayset.png
rm ~/.local/share/applications/wayset.desktop

sudo rm /etc/systemd/system/wayset.service

sudo systemctl daemon-reload
