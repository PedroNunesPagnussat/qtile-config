from settings.vars import colors
from libqtile.layout.bsp import Bsp
from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadTall, MonadThreeCol
from libqtile.layout.max import Max
from libqtile.layout.floating import Floating
from libqtile.config import Match

layout_theme = {
    "border_width": 4,
    "margin": 10,
    "border_focus": colors[8],
    "border_normal": colors[0],
}

layouts = [
    Columns(**layout_theme),  # Free Movement
    Bsp(**layout_theme),  # Square
    MonadTall(**layout_theme),  # One Master Windown
    MonadThreeCol(**layout_theme),  # Three Columns
    Max(border_width=0, margin=0),  # Full Screen
]

floating_layout = Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    **layout_theme
)

#
#
# More layouts can be found on libqtile.layout
#
#
# Try more layouts by unleashing below layouts.
# layout.Stack(num_stacks=2),
# layout.Max(),
# layout.MonadTall(),
# layout.MonadWide(),
# layout.RatioTile(),
# layout.Tile(),
# layout.TreeTab(),
# layout.VerticalTile(),
# layout.Zoomy(),
# layout.Matrix(),
