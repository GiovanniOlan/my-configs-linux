# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os

mod = "mod4"
terminal = guess_terminal()

color = {
    'white' : '#ffffff',
    'black' : '#000000',
    'blue'  : '#8eb3ed',
    'red'   : '#ed3e3e',
    'morado': '#ab04cc',
}
FONT_SIZE = 20

def draw_medium_circle(tipo, _bg):
    icono = ""
    if tipo==1:
        icono = ""
    else:
        icono = ""
    
    return widget.TextBox(
        text       = icono, 
        fontsize   = FONT_SIZE+10,
        foreground = _bg,
        padding    = 0,
    )

def insert_text(text, _bg, _foreground, _fontsize):    
    return widget.TextBox(
        text       = text, 
        fontsize   = _fontsize,
        background = _bg,
        foreground = _foreground,
    )

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    

    #My shortcuts
    Key([mod], "x", lazy.spawn("rofi -show run"), desc="Launch Rofi"),
    Key([mod], "b", lazy.spawn("brave"), desc="Launch brave"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch code"),
    Key([mod], "p", lazy.spawn("pavucontrol"), desc="Launch PavoControl"),
    # Key([mod], "s", lazy.spawn("gnome-screenshot -i"), desc="Take ScreenShoot"),
    Key([mod], "s", lazy.spawn("scrot -s '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'"), desc="Take ScreenShoot"),
    Key([mod, 'shift'], "s", lazy.spawn("gnome-screenshot -i"), desc="Take ScreenShoot"),

]

groups = [Group(i) for i in [
    "  ", "  ", "  ", "  ", "  ", "  ", " 雷 ", "  ", "  ",  
    # "  ", "  ", "  ", "  ", "  ", "  ", " 雷 " 
]]

for i,group in enumerate(groups):
    numeroEscritorio = str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                numeroEscritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numeroEscritorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus= color['white'], 
        border_width=1
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                insert_text(" ", color['black'], color['black'], FONT_SIZE+10),

                #widget.CurrentLayout(),
                draw_medium_circle(0, color['white']),
                widget.GroupBox(
                    inactive = color['black'],
                    active = color['morado'],
                    background = color["white"],
                    fontsize   = FONT_SIZE+5,
                    foreground = color["black"],
                    padding    = 15,
                    highlight_method='line',
                    highlight_color = [color['blue'],color['blue']],
                    other_screen_border = color['morado'], 
                    other_current_screen_border = color['blue'],
                ),
                draw_medium_circle(1, color['white']),
                #widget.Prompt(),
                insert_text(" ", color['black'], color['black'], FONT_SIZE+10),

                draw_medium_circle(0, color['white']),
                insert_text("  ", color['white'], color['morado'], FONT_SIZE),
                widget.WindowName(
                    background = color['white'],
                    fontsize   = FONT_SIZE-8,
                    foreground = color['black'],

                ),
                draw_medium_circle(1, color['white']),
                insert_text(" ", color['black'], color['black'], FONT_SIZE),


                #widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                #widget.Systray(),
                draw_medium_circle(0, color['white']),
                insert_text("  ", color['white'], color['morado'],FONT_SIZE),
                widget.CPU(
                    background = color['white'],
                    foreground = color['black'],
                ),
                insert_text(" 直 ", color['white'], color['morado'], FONT_SIZE+10),
                widget.Net(
                    foreground = color['black'],
                    background = color['white'],
                    prefix     = 'M',
                    format     = '{down}',
                ),
                draw_medium_circle(1, color['white']),

                insert_text(" ", color['black'], color['black'], FONT_SIZE+10),


                draw_medium_circle(0, color['white']),
                insert_text("  ", color['white'], color['morado'],FONT_SIZE),
                widget.Clock(
                    font = "Anonymice NF",
                    format="%a %I:%M%p %d-%m-%Y",
                    background = color['white'],
                    foreground = color['black'],
                    fontsize = FONT_SIZE-5,
                    padding = 5, 
                ),
                draw_medium_circle(1, color['white']),

                insert_text(" ", color['black'], color['black'], FONT_SIZE+10),


                #widget.QuickExit(),
            ],
            24,
            border_width=[10, 0, 10, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = [

    "feh --bg-fill ~/my-configs-linux/Qtile/wallpaper/archlinux-wallpaper.jpg",  
    "picom --no-vsync &",
    "setxkbmap -layout us -variant intl",
    'export PATH="/home/debian-gio/miniconda3/bin:$PATH"',
    'source ~/miniconda3/etc/profile.d/conda.sh',
]

for x in autostart:
    os.system(x)


