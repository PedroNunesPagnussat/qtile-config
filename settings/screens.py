from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from .widgets import default_widgets
import subprocess


def status_bar(widgets):
    return bar.Bar(widgets, 30)


screens = [Screen(top=status_bar(default_widgets))]
