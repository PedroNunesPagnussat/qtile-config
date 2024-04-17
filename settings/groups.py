from libqtile.command import lazy
from libqtile.config import Group, Key

from settings.keybindings import keys, mod

# TODO MAKE THE DICT BE THE CONFIG AND MAKE THE FUCKING THING WORK
#
# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

# Layout names
default_layout = "monadtall"
equal_split_layout = "bsp"
full_screen_layout = "max"
free_move_layout = "columns"
tree_columns_layout = "monadthreecol"

#     
group_definition = [
    {"label": "  ", "name": 1, "layout": default_layout},  #     
    {"label": " 󰊯 ", "name": 2, "layout": default_layout},
    {"label": "  ", "name": 3, "layout": equal_split_layout},
    {"label": " 󰙯 ", "name": 4, "layout": full_screen_layout},  # 󰭹 Option
    {"label": " 󰝚 ", "name": 5, "layout": default_layout},
    {"label": " 󰨞 ", "name": 6, "layout": default_layout},  # 󰨞  
    {"label": "  ", "name": 7, "layout": default_layout},
    {"label": "  ", "name": 8, "layout": full_screen_layout},
    {"label": "  ", "name": 9, "layout": equal_split_layout},
]

groups = [Group(definition["label"], layout=definition["layout"]) for definition in group_definition]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend(
        [
            # Switch to workspace N
            Key(
                [mod],
                actual_key,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # Send window to workspace N
            Key(
                [mod, "shift"],
                actual_key,
                lazy.window.togroup(group.name),
                desc="Move focused window to group {}".format(group.name),
            ),
        ]
    )
