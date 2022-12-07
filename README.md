# window-switcher-workaround
window switcher workaround for KDE Plasma


### Description
```
This script will move to the next/previous window on the current desktop in the order the windows are opened. I was trying to make it move in the order of the KDE Plasma Task Manager but I couldn't find a way to get the order of it's window icons via the command line. So for now I'm just set the KDE Task Manager's Sorting Behavior to "Do not sort" (which defaults to the order the windows are opened) by doing:
	*right click Task Manager* > Configure Icons-only Task Managaer ... > Behavior > Sort > Do no sort
If anyone knows hows to get the order of the Task Manager please let me know!

```

### Setup
```
git clone git@github.com:PopeyedLocket/window-switcher-workaround.git
System Settings > Shortcuts > Custom Shortcuts > Edit > New > Global Shortcut > Command/URL
name it something like "switch window right"
set the shortcut Trigger to any key combination you want, such as Ctrl + Alt + RightArrow
set the shortcut Action to: /usr/bin/python3 /<path>/<to>/window-switcher-workaround/main.py next
create another shortcut with a different trigger and
set the shortcut Action to: /usr/bin/python3 /<path>/<to>/window-switcher-workaround/main.py prev
```

