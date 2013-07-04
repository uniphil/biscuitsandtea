%%%
#How to make Conkys forward click events

Make sure you have the following line in your conkyrc:

```
own_window_type override
```
The 'Override-Redirect' window type redirects all events to the window's parent
(in my case, the root window/desktop).
%%%

![A picture of a transparent desktop Conky with drop shadows]({{ url_for('media', filename='conky_with_shadow.png' )}}){: title="Conky with shadow" class="floatright"}
![A picture of a transparent desktop Conky without drop shadows]({{ url_for('media', filename='conky_without_shadow.png' )}}){: title="Conky without shadow" class="floatright"}

Setting the conky to be this window type from the default 'desktop' window
type, made my composite engine, [compton](https://github.com/chjj/compton "Compton Github Page"), give shadows to my Conkys, which I did not like.


Conveniently, compton has an option `--shadow-exclude CONDITION` that can exclude
rendering drop-shadows on windows of a certain based on CONDITION. See the
[manpage](https://github.com/chjj/compton/blob/master/man/compton.1.asciidoc "Compton Github Manpage")
for all the formatting options for CONDITION. To exclude all Override-Redirect
windows from getting shadows, the form is:
```
compton ... --shadow-exclude 'override_redirect'
```