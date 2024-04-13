from libqtile.command import lazy
from libqtile.config import Group, Key

from settings.keybindings import keys, mod

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
groups = [
    Group(i)
    for i in [
        "  ",
        " 󰊯 ",
        " 󰙯 ",  # 󰭹 Option
        "  ",
        "  ",
        " 󰝚 ",
    ]
]

# 
group_definition = [
    {"name": "  ", "key": 1, "layouy": 1},
    {"name": " 󰊯 ", "key": 2, "layouy": 1},
    {"name": " 󰙯 ", "key": 3, "layouy": 1},  # 󰭹 Option
    {"name": "  ", "key": 4, "layouy": 1},
    {"name": "  ", "key": 5, "layouy": 1},
    {"name": " 󰝚 ", "key": 6, "layouy": 1},
]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend(
        [
            # Switch to workspace N
            Key([mod], actual_key, lazy.group[group.name].toscreen()),
            # Send window to workspace N
            Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
        ]
    )
