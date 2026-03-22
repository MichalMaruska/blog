---
title: "Keeping up with debian Sid"
date: 2017-09-11
draft: false
---

# Keeping up with debian Sid

## My small build system

I need to replace some distro packages with my improvements.

For this I need to patch the sources -- I only handle git. I need to be notified, warned, when a new version is needed.  
  
So I patched [apt](https://github.com/mmaruska/apt/commits/maruska) to report when a switch from my version to the upstream would happen (due to  "**apt dist-upgrade").**  
  
In such a case I run my  [git-rebase-origin](https://github.com/mmaruska/git-hierarchy) which rebases my feature poset (of feature branches/segments mixed into "merges") over a refreshed remote branch.  
  
Then I run [my scripts](https://github.com/mmaruska/mmc-build-system) to invoke [gbp](http://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html)(1) with a suitable version string, and create the deb packages & put them in reprepro.  
  
the sequence of commands to maintain apt itself:  
  
  
**$ cd ~/git/apt/  
$ git-rebase-origin**  
# this deduces the upstream -- base of my feature branches.

**$ release**  
# this detects I'm building my extension of upstream debian package, so deduces the correct version, build, uploads, tags, pushes, installs.  
  
When I only want to test some changes, I run

$ **snap**

which creates a .deb package, installs it, withouth any reprepro etc.
