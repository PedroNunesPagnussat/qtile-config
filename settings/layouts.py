from theme.colors import catppuccin_mocha
from libqtile.layout.bsp import Bsp
from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadTall, MonadThreeCol


colors = catppuccin_mocha

layout_theme = {
    "border_width": 2,
    "margin": 10,
    "border_focus": colors[8],
    "border_normal": colors[0],
}

layouts = [
    Columns(**layout_theme),  # Free Movement
    Bsp(**layout_theme),  # Square
    MonadTall(**layout_theme),  # One Master Windown
    MonadThreeCol(**layout_theme),  # Three Columns
]


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
