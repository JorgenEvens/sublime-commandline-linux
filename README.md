# sublime-commandline-linux

This plugin works around a somewhat annoying issue when using the commandline on linux to launch Sublime Text 2 in a specific folder.

When you would `sublime <folder>`, 2 windows would appear, your previous session and the new one.
This plugin closes the old one for you.

## Installation

### Sublime script
Copy the `sublime` script into your `/usr/bin` or add it to your `PATH` environment variable.

`cp sublime /usr/bin/sublime`

### Sublime plugin
Drop `CommandLineFix.py` in your plugin directory which usually is `~/.config/sublime-text-2/Packages/User`.

`cp CommandLineFix.py ~/.config/sublime-text-2/Packages/User/`

### Done
You should be able to launch sublime from commandline using the command `sublime .` without having to deal with your previous session.