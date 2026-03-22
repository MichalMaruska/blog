---
title: "Forking -- multitouch on keyboard"
date: 2014-08-19
draft: false
---

# Forking -- multitouch on keyboard

Multitouch on keyboard is about ... interpreting simultaneous key presses  
in a way that is different from sequential.  
  
That is pressing 2 keys A+B should be something different from A, followed by B.  
Years ago, I was told focus on the problem of converting one of the  
letters into a modifier, and keep B as is. This has been enough of challenge to implement (properly), and I can share the software now.  
  
The implementation includes patches to several components of the X-Windows system,
and configuration tools.  
  
Here's a diagram of involved parts:  
  

  
  
The most complex part is extension of the Xorg server, to somehow postpone processing key events *while* maintaining the semantics of Un/Grab requests.  
  
Since we use the timing of key events, we want to get best precision timestamps on them. Xorg server has to get the monotonic timestamp from the kernel/evdev.  
That implies a bit of patches to input driver(xorg-evdev), and the DDX code to accepts events and put them into the event queue.  
  
From there we want to plug this new functionality in the heap of machinery which implements auto-repeat, other XKB functionality, and then the Grab/Ungrab ops.  
  
I have tried to separate, serialize the implementation of these functionalities, using this simple architecture: a linked list of  blocks with this API:  
 (image missing)  
  
These blocks pass Events  to the next one (in one direction), and in the other direction the information about Grab/Ungrab state is passed.  
  
Indeed, if no event comes in, time can still be "pushed" through all these plugins,  
so a plugin can also tell how early it is significant to push time to it.  
  
(work-in-progress).
