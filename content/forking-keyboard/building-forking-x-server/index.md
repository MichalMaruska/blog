---
title: "Building the Forking X server"
date: 2014-10-16
draft: false
---

# Building the Forking X server

## Building the Forking X server

I work on Debian (Sid), so the Git repositories contain debian/ and  packages are built by git-buildpackage as documented in another post.

You can also install by using my debian repository:  
deb http://www.ruska.it/~michal/reprepro sid main  
  
I did not implement a new Extension - I extended the protocol of XKB.  
So, first build the x11proto-kb-dev package  

* https://github.com/mmaruska/x11proto-kb

Now it's possible to build both libX11 and the server:

* https://github.com/mmaruska/xserver

Since the ABI between the server and "input device" driver, it's necessary to recompile them. I use only evdev & synaptics. But, evdev is used for the keyboard, and I need precise timestamps, so there are changes, hence build from this repo:

* https://github.com/mmaruska/xserver-xorg-input-evdev

At this point the Xserver could be restarted. After building the X11 from:

* https://github.com/mmaruska/libX11.git  
    
  one can start asking the X server about the active plugins. There is a tool for that:

* https://github.com/mmaruska/xplugin

At this point it is possible to:

$ xinput list

....Virtual core keyboard                       id=3    [master keyboard (2)]

...

$  xplugin -l -d 3

3 plugins in the pipeline

1: never-freeze-queue

2: xkb-auto-repeat

0: core

#### The function of each plugin:

**never-freeze-queue** collects events while waiting for following plugins to proceed (& accept the events).  **xkb-auto-repeat** generates the auto-repeat events, **core** is the interface with dix/events.c.

Now we can finaly build the interesting feature: the "**fork**" plugin to be inserted before the auto-repeat plugin. It is implemented in C++ which explains some effort in the X server and x11proto-kb sources to make them C++ compatible.

So:

* https://github.com/mmaruska/fork-plugin

so after building (& installing) you can insert that plugin:

$ xplugin -d 3 fork       # 3 is still the id of keyboard.  
or also remove it:  
$ xplugin -d 3 -fork

Now to activate some of the forks we need to communicate with that plugin,

and build up a language to express the configuration.

* https://github.com/mmaruska/libfork

For the configuration language, I chose to use Scheme, in the Gauche implementation. So, one needs to install Gauche-dev, and build this binding module:

* https://github.com/mmaruska/gauche-xlib

building that one is more involved (see my blog about building Gauche modules).

That packages contains my configuration to be used this way:

$ fork-config-mmc.scm 3

When trying to configure, keep in mind, that allocation of the "fork" keycodes

is possible only if the XKB Geometry allows it. I.e. keycodes not found on the Geometry will be used.

See in https://github.com/mmaruska/gauche-xlib/blob/master/bin/fork-config-mmc.scm how key "f" is used as Hyper modifier, or how Meta key acts as Escape key.
