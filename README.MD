```bash

sudo apt install xserver-xorg xinit
sudo apt install libpangocairo-1.0-0
sudo apt install python3-pip python3-xcffib python3-cairocffi
pip install qtile

echo 'export PATH="~/.local/bin:$PATH"' >> ~/.bashrc 

echo "[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Exec=qtile start
Type=Application
Keywords=wm;tiling" | sudo tee /usr/share/xsessions/qtile.desktop

gnome-session-quit
```
