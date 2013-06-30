HowTo make your Conkys transparent to your clicks. (event forwarding)

Make sure you have the following lines in your conkyrc:

```
own_window_type override
```
The 'Override-Redirect' window type redirects all events to the window's parent
(in my case, the root window/desktop).

Setting the conky to be this window type from the default 'desktop' window
type, made my composite engine, [compton](https://github.com/chjj/compton "Compton Github Page"),
give shadows to my Conkys, which I did not like.

Conveniently, compton has an option `--shadow-exclude CONDITION` that can exclude
rendering drop-shadows on windows of a certain based on CONDITION. See the
[manpage](https://github.com/chjj/compton/blob/master/man/compton.1.asciidoc "Compton Github Manpage")
for all the formatting options for CONDITION. To exclude all Override-Redirect
windows from getting shadows, the form is:
```
compton ... --shadow-exclude 'override_redirect'
```