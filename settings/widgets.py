from libqtile import widget

from settings.vars import colors

font_default = {
    "font": "JetBrainsMono Nerd Font Mono Regular",
    "fontsize": 16,
}


def ConfigCurrentLayoutIcon():
    return widget.CurrentLayoutIcon(
        # custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
        foreground=colors[1],
        padding=4,
        scale=0.6,
        **font_default,
    )


def ConfigCurrentLayout():
    return widget.CurrentLayout(
        foreground=colors[1],
        background=colors[0],
        padding=4,
        scale=0.6,
        **font_default,
    )


def ConfigGroupBox():
    return widget.GroupBox(
        margin_y=5,
        margin_x=0,
        padding_y=0,
        padding_x=0,
        borderwidth=3,
        active=colors[1],
        inactive=colors[8],
        rounded=False,
        highlight_color=colors[2],
        # highlight_method="text", THAT IS ALSO COOL
        highlight_method="line",
        this_current_screen_border=colors[7],
        this_screen_border=colors[4],
        other_current_screen_border=colors[7],
        other_screen_border=colors[4],
        **font_default,
    )


def ConfigPrompt():
    return widget.CurrentLayoutIcon(
        # custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
        foreground=colors[1],
        padding=4,
        scale=0.6,
        **font_default,
    )


def ConfigWindowName():
    return widget.WindowName(
        foreground=colors[1],
        max_chars=40,
        **font_default,
    )


def ConfigTextBox(text, color):
    return widget.TextBox(
        text=text,
        foreground=color,
        padding=2,
        **font_default,
    )


def ConfigSpacer(lenght):
    return widget.Spacer(lenght=lenght)


def ConfigClock():
    return widget.Clock(
        foreground=colors[1],
        format="⏱  %a, %d/%m - %H:%M ",
        **font_default,
        # decorations=[
        #     BorderDecoration(
        #         colour=colors[8],
        #         border_width=[0, 0, 2, 0],
        #     )
        # ],
    )


def ConfigCPU():
    return widget.CPU(format="▓  Cpu: {load_percent}%", foreground=colors[4], **font_default)


def ConfigMemory():
    return widget.Memory(
        foreground=colors[9],
        # mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
        format="{MemUsed: .0f}{mm}",
        fmt="🖥  Mem: {}",
        **font_default,
    )


def ConfigDisk():
    return widget.DF(
        update_interval=60,
        foreground=colors[5],
        # mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e df")},
        partition="/",
        # format = '[{p}] {uf}{m} ({r:.0f}%)',
        format="{uf}{m}",
        fmt=" Disk: {}",
        visible_on_warn=False,
        **font_default,
    )


def ConfigVolume():
    return widget.Volume(
        foreground=colors[7],
        fmt=" Vol: {}",
        **font_default,
    )


def ConfigKeyBoard():
    return widget.KeyboardLayout(
        foreground=colors[4],
        fmt="⌨  Kbd: {}",
    )


widget_defaults = dict(font="JetBrainsMono Nerd Font Mono Regular", fontsize=16, padding=0, background=colors[0])
extension_defaults = widget_defaults.copy()

default_widgets = [
    ConfigGroupBox(),
    ConfigTextBox("|", colors[8]),
    ConfigCurrentLayoutIcon(),
    ConfigCurrentLayout(),
    ConfigTextBox("|", colors[8]),
    # ConfigPrompt(),
    ConfigWindowName(),
    ConfigCPU(),
    ConfigMemory(),
    ConfigDisk(),
    ConfigVolume(),
    ConfigKeyBoard(),
    # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground=colors[7], **widget_defaults),
    # widget.Systray(**widget_defaults),
    ConfigClock(),
    widget.QuickExit(**widget_defaults, foreground=colors[3]),
    # TODO MEMORY CPU
    # TODO WIFI
]
