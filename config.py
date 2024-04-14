from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# groups
from settings.groups import groups

# keybindings
from settings.keybindings import keys

# Variables such as term and mod
from settings.vars import mod, terminal

# Layouts
from settings.layouts import layouts, floating_layout

# Color theme
from theme.colors import catppuccin_mocha

# Mouse
from settings.mouse import mouse


# TODO ADD ROFI INSTALL SCRIPT
# MAKE GROUPS BETTER

# TODO start widget

from settings.screens import screens
from settings.widgets import default_widgets


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
