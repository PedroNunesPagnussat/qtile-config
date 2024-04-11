from libqtile.config import Key
from libqtile.lazy import lazy
from settings.vars import mod, terminal


# A list of available commands that can be bound to keys can be found
# at https://docs.qtile.org/en/latest/manual/config/lazy.html


keys = [
    #
    # Switch between windows
    #
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    #
    # Move the position of the windows in the stack
    #
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    #
    # Resize windows
    #
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    #
    # Layout and Windoe Layouts
    #
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),  # TODO CHECK
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    #
    # Kills and Startups
    #
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),  # TODO ADD ROFI
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    #
    # Qtile
    #
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "Return", lazy.layout.toggle_split(), desc="Overlay stack with the current"),
    #
    # CHECK THIS
    #
    #     # Switch focus of monitors
    # ([mod], "period", lazy.next_screen()),
    # ([mod], "comma", lazy.prev_screen()),
    #
    #     # Volume
    # ([], "XF86AudioLowerVolume", lazy.spawn(
    #     "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    # )),
    # ([], "XF86AudioRaiseVolume", lazy.spawn(
    #     "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    # )),
    # ([], "XF86AudioMute", lazy.spawn(
    #     "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    # )),
    #
    # # Brightness
    # ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    # ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    #
]
