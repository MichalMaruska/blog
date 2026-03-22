---
title: "Building Emacs from Git, with some extensions"
date: 2012-11-22
draft: true
---

# Building Emacs from Git, with some extensions

\* How I build Emacs from Git, with my modifications  
  
  
\*\* I pull from Julien Danjou's Git repository -- it has the debian packaging patches. He pulls from bzr upstream.  
  
  
\*\* I move "base" branch to the last debian-unstable release.  
  
git branch -f base debian-unstable.  
  
  
\*\* I rebase all my segments/sums atop the newly moved "base"  
  
git-rebase-poset  
  
  
\*\* I added the debian-patches branch as a segment, and included  
it in the mmc-all sum:  
  
  
git branch debian-patches 4a2cb3e5d57929e5d3681ac55a241c7c68021ee0  
git rebase  --onto base  debian-patches~11 debian-patches  
  
I solved some conflicts.  
  
I declare this new branch as a segment:  
  
> git-segment debian-patches heads/base  
> git-sum mmc-all +debian-patches  
  
I can, but I can do that later, rebase:  
> git-rebase-poset  
  
  
Then I had to patch some more to avoid a problem with  
"image-load-path undefined"  
So, a segment upon the sum:  
  
git-segment mmc-final-fixes heads/mmc-all  
git revert 5aea9c3d8e822831f0209508fa72ce1a195334d7  
  
  
Then I built, and installed the emacs-snapshot-xlib package.  
  
  
  
Current problems with git-hierarchy:  
After pushing into a remote repo, all symbolic links are turned  
into absolute ones.
