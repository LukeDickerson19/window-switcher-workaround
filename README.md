# window-switcher-workaround
window switcher workaround for KDE Plasma


### Description
```
This script will move to the left/right window on the KDE Plasma Task Manager, allowing
one to assign a keyboard shortcut to the execution of this script, with the caveat that
one must set the KDE Task Manager's Sorting Behavior to "Do not sort" (which defaults to
the order the windows are opened).

I was trying to make it move in the order of the KDE Plasma Task Manager itself but I
couldn't find a way to get the order of it's window icons via the command line. If
anyone knows hows to get the order of the Task Manager please let me know (so we could
use "Manual Sort" instead of "Do not sort" :D)!


NOTE: This script only works on Xorg due to it's dependency on wmctrl.

UPDATE April 14 2024: added desktop_next and desktop_prev script args for feature to
switch desktops as well.

```

### Setup
```
right click Task Manager > Configure Task Manager ... > Behavior > Sort > Do no sort

open termal and run this command where ever you want to store this script
git clone git@github.com:LukeDickerson19/window-switcher-workaround.git

open System Settings and go to
Shortcuts > Custom Shortcuts > Edit > New > Global Shortcut > Command/URL
name it something like "switch window right"
set the shortcut Trigger to any key combination you want, such as Meta + RightArrow
set the shortcut Action to:
	/usr/bin/python3 /path/to/window-switcher-workaround/main.py next
create another shortcut with a different trigger and
set the shortcut Action to:
	/usr/bin/python3 /path/to/window-switcher-workaround/main.py prev
if you want to be super organized you can create a group called "window switcher"
and move these 2 shortcuts inside it
```

### Sources
```
https://www.reddit.com/r/kde/comments/puh76y/switch_windows_in_order_of_task_bar/
https://askubuntu.com/questions/873521/how-can-i-cycle-windows-in-taskbar-order/873943#873943
https://www.reddit.com/r/kde/comments/sp5k1u/comment/i6p07j6/?utm_source=share&utm_medium=web2x&context=3
https://bugs.kde.org/show_bug.cgi?id=391174
https://docs.kde.org/trunk5/en/kwin/kcontrol/kwintabbox/kwintabbox.pdf
	"Stacking Order is the order in which the windows appear on the screen"
```