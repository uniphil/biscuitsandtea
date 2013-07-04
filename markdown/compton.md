%%%
#My Compton command:
Compton my compositor of choice. It adds simple elegance to a window manager like Openbox.
```bash
compton -cCGbz --config /dev/null --shadow-exclude 'override_redirect \
|| class_g = "Synapse"' --backend glx
```
%%%

Breakdown of options:
`-c`:
Enables shadows on windows (note that windows with `_NET_WM_WINDOW_TYPE_DESKTOP`
never get shadow)

`-C`:
Avoid drawing shadows on dock/panel windows (works on Tint2).

`-G`:
Don't draw shadows on drag-and-drop windows. (This means all text, file
dragging - they look rather silly without this option)

`-b`:
Daemonize process. (Fork to background process). This is useful when you run
Compton from a script you don't want halted.

`-z`:
This clears the drop-shadow from behind windows, so that the only shadow is on the exterior edge. The difference is best explained with a screenshot:

with:

![LXTerminal composited with Compton with -z" style="float:right" src="{{ url_for('media', filename='compton_transparent_terminal.png') }}" alt="A transparent LXTerminal window is shown composited with the compton -z option. The shadow only appears outside the purely transparent rectangular area, yielding sharp edges.]({{ url_for('media', filename='compton_transparent_terminal.png') }} LXTerminal composited with Compton with -z)

and without:

![A transparent LXterminal window is shown composited with compton without the option -z; the shadow is painted over the entire area of transparency.]({{ url_for('media', filename='compton_transparent_terminal_shadow.png') }} LXTerminal composited with Compton without -z)

(see Compton's
[FAQ#6](https://github.com/chjj/compton/wiki/faq "Compton FAQ on Github"))
This matters with transparent or semi-transparent ARGB windows.

`--config /dev/null`:
Points to the configuration file (in my case, I have none, so I point it to
/dev/null).

`--shadow-exclude 'override_redirect || class_g = "Synapse"'`:
Ensures shadows are not drawn on windows of type Override-Redirect, or windows
with class Synapse.
Protip: to find a window's class, or other information use `xwininfo`
