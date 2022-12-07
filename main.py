import sys
import subprocess


# parse arg
if len(sys.argv) < 2: sys.exit()
direction = 0
if sys.argv[1] == 'next': direction = 1
if sys.argv[1] == 'prev': direction = -1
if direction == 0: sys.exit()


def get_command_output(cmd):
	return subprocess.check_output(
		cmd.split(' ')).decode("utf-8").strip()

def get_current_desktop():
	desktop_info = get_command_output('wmctrl -d')
	for d in desktop_info.splitlines():
		d_info = list(filter(None, d.split(' ')))
		if d_info[1] == '*':
			desktop_id = d_info[0]
			# print(desktop_id)
			return desktop_id

def get_windows_on_desktop(desktop_id):
	window_info = get_command_output('wmctrl -l')
	window_ids = []
	for w in window_info.splitlines():
		w_info = list(filter(None, w.split(' ')))
		if w_info[1] == desktop_id:
			w_id = w_info[0]
			# w_name = ' '.join(w_info[3:])
			# print(w_id, w_name)
			window_ids.append(w_id)
			# window_ids[w_id] = w_name
	# window_ids = [v for k, v in sorted(window_ids.items(), key=lambda item: item[1])]
	# window_ids = list(window_ids.values())
	# for w in window_ids: print(w)
	return window_ids

def get_current_window():

	# get current window hex id
	xprop_info = get_command_output('xprop -root')
	current_window_id = [line.split()[-1] \
		for line in xprop_info.splitlines() \
		if '_NET_ACTIVE_WINDOW(WINDOW)' in line][0]

	# convert xprop- format for window id to wmctrl format
	current_window_id = \
		current_window_id[:2] + \
		((10 - len(current_window_id))*'0') + \
		current_window_id[2:]

	# print(current_window_id)
	return current_window_id

def move_to_window(window_id):
	subprocess.check_output(
		('wmctrl -i -a %s' % window_id).split(' '))

''' TODO:
	couldn't find this info, if i could get it then I wouldn't have to set the KDE Task Manager's Sorting Behavior to "Do not sort"
	*right click Task Manager* > Configure Icons-only Task Managaer ... > Behavior > Sort
	'''
def get_task_manager_window_order():
	pass


if __name__ == "__main__":
	current_desktop = get_current_desktop()
	windows = get_windows_on_desktop(current_desktop)
	current_window = get_current_window()
	current_window_index = windows.index(current_window)
	new_window = windows[(current_window_index + direction) % len(windows)]
	move_to_window(new_window)
