import os
import subprocess

from libqtile import hook

# groups
from settings.groups import groups

# keybindings
from settings.keybindings import keys

# Layouts
from settings.layouts import floating_layout, layouts

# Mouse
from settings.mouse import mouse
from settings.screens import screens

# Variables such as term and mod
from settings.vars import mod, terminal
from settings.widgets import default_widgets

# Color theme
from theme.colors import catppuccin_mocha

# TODO ADD ROFI INSTALL SCRIPT
# MAKE GROUPS BETTER
# Improve floating layouts
# Improve widgets


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


start_once()

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
