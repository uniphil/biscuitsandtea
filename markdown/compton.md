My Compton command:
```bash
compton -cCGbz --config /dev/null --shadow-exclude 'override_redirect ||
class_g = "Synapse"' --backend glx
```

Breakdown of options:
-c:
Enables shadows on windows (note that windows with _NET_WM_WINDOW_TYPE_DESKTOP
never get shadow)

-C:
Avoid drawing shadows on dock/panel windows (works on Tint2).

-G:
Don't draw shadows on drag-and-drop windows. (This means all text, file
dragging - they look rather silly without this option)

-b:
Daemonize process. (Fork to background process). This is useful when you run
Compton from a script you don't want halted.

-z:
This clears the drop-shadow from behind windows (so the only shadow is on the
exterior edge). This is best explained with a screenshot (see
*FAQ#6(https://github.com/chjj/compton/wiki/faq)*)
This matters with transparent or semi-transparent ARGB windows.

--config /dev/null:
Points to the configuration file (in my case, I have none, so I point it to
/dev/null).

--shadow-exclude 'override_redirect || class_g = "Synapse"':
Ensures shadows are not drawn on windows of type Override-Redirect, or windows
with class Synapse.
Protip: to find a window's class, or other information use `xwininfo`
