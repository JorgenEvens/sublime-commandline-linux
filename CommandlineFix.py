import sublime, sublime_plugin
import sys

def FixExtraWindows():
	windows = sublime.windows()
	active = sublime.active_window()

	for w in windows:
		if w.id() != active.id():
			w.run_command('close_window')

sublime.set_timeout( FixExtraWindows, 50 )
