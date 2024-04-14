import sys
import subprocess


# parse arg
if len(sys.argv) < 2: sys.exit()
window_direction = 0
desktop_direction = 0
if sys.argv[1] == 'next': window_direction = 1
if sys.argv[1] == 'prev': window_direction = -1
if sys.argv[1] == 'desktop_next': desktop_direction = 1
if sys.argv[1] == 'desktop_prev': desktop_direction = -1
if window_direction == 0 and desktop_direction == 0: sys.exit()


def get_command_output(cmd):
	return subprocess.check_output(
		cmd.split(' ')).decode("utf-8").strip()

def get_current_desktop():
	desktop_info = get_command_output('wmctrl -d').splitlines()
	num_desktops = len(desktop_info)
	for d in desktop_info:
		d_info = list(filter(None, d.split(' ')))
		if d_info[1] == '*':
			desktop_id = int(d_info[0])
			# print(desktop_id)
			return desktop_id, num_desktops

def get_windows_on_desktop(desktop_id):
	window_info = get_command_output('wmctrl -l')
	window_ids = []
	for w in window_info.splitlines():
		w_info = list(filter(None, w.split(' ')))
		if int(w_info[1]) == desktop_id:
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
		('wmctrl -ia %s' % window_id).split(' '))

''' TODO:
	couldn't find this info, if i could, I wouldn't have to set the KDE Task Manager's Sorting Behavior to "Do not sort"
	*right click Task Manager* > Configure Icons-only Task Managaer ... > Behavior > Sort
	'''
def get_task_manager_window_order():
	pass

def move_to_desktop(new_desktop):
	subprocess.check_output(
		('wmctrl -s %s' % new_desktop).split(' '))

''' TODO:
	couldn't find this info, if i could, this script could work for 
	'''
def get_desktop_layout():
	# number of rows
	# number of cols
	pass


if __name__ == "__main__":
	if window_direction != 0:
		current_desktop, _ = get_current_desktop()
		windows = get_windows_on_desktop(current_desktop)
		current_window = get_current_window()
		current_window_index = windows.index(current_window)
		new_window = windows[(current_window_index + window_direction) % len(windows)]
		move_to_window(new_window)
	elif desktop_direction != 0:
		current_desktop_index, num_desktops = get_current_desktop()
		new_desktop = current_desktop_index + desktop_direction
		if 0 <= new_desktop < num_desktops:
			move_to_desktop(new_desktop)

