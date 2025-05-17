#!/bin/bash

sudo systemctl stop wayset

pip install --break-system-packages keyboard | pip3 install --break-system-packages keyboard
sudo pip install --break-system-packages keyboard | sudo pip3 install --break-system-packages keyboard

chmod +x wayset

sudo cp wayset /usr/local/bin/wayset
sudo cp -r usr /
cp wayset.desktop ~/.local/share/applications/wayset.desktop

sudo cp wayset.service /etc/systemd/system/wayset.service
sudo chmod 777  /etc/systemd/system/wayset.service

sudo systemctl enable wayset
sudo systemctl daemon-reload
sudo systemctl start wayset

