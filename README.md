Move Tabs
=========================

for [Sublime Text 2][0] or [3][3]

-------------

Ever wanted to move tabs around in Sublime Text with your keyboard?  
Well, I did. And now you can, too!

## Installation

**Step 1** -- Go get wbond's beautifully simple [Sublime Package-Control][2].  
**Step 2** -- Hit `ctrl+shift+p` (Windows, Linux) or `cmd+shift+p` (OSX), run the `install package` command.  
**Step 3** -- Search for and install _Move Tabs_.

**Step 4** -- Win and/or Profit.

-----

## Usage

#### The Short

Do you have more than one view open as a tab?  
Is this plug-in installed?  
Press `ctrl+shift+pageup`.

Unless you're on a Mac, in which case you should press `command+shift+p` and search for `Move File in Group Left`.  
It's hard to find keybindings for Macs!


#### The Long

This plug-in adds two commands Sublime Text which expose easy-to-hotkey tab shuffling. On Windows and Linux I took a leaf from Linux's book and added the `ctrl+shift+[pageup|pagedown]` hotkeys, in similar form to those used to shift tabs in your terminal. My Mac doesn't have pageup/down keys so I was at a loss for what to do there.  
On all platforms -- most notably Macs -- there are two new commands searchable through the `ctrl+shift+p` (on Windows/Linux) or `command+shift+p` (on Macs) overlay, `Move File in Group Left` and `Move File in Group Right`, which reference the same underlying commands.

The aforementioned commands this plug-in adds are:

    "command": "move_tab_left"
    "command": "move_tab_right"

That's really all there is to it.

Enjoy.

-----

**This project is open under the [MIT License][1]**


 [0]: http://www.sublimetext.com/2
 [1]: http://revolunet.mit-license.org
 [2]: http://wbond.net/sublime_packages/package_control
 [3]: http://www.sublimetext.com/3
