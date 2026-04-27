---
title: "Using github: building on github"
date: 2026-04-27
draft: false
---

# Further steps to deletegate to Github


## I started to build on GH

All I need is debian packages, collected in my repository (reprepro).

### Initial state:
doing both on my machines, and exporting the reprepro (pool, dists) to GH as git, to have
it published as gh-pages. But that meant that building on Arm64 required its own clone
of the reprepro (git repo), and a way to sync them (maintain the db/ part of reprepro),
and avoid rebuilding arch-independent packages -- unfortunately still not identically --
on both amd64 and arm64.


### Start: let's try to see if it works at all
and push to the reprepro all from the workflow! Give it GPG key (to sign reprepro), SSH key to access
the central reprepro repository on GH.


### Immediately reprepro is needed.
It should not be pushing the packages, but instead schedule a job on the "apt-repo", which retrieves
the "release artifacts".


### all the satellites -- repositories with debian packages -- repeat the same workflow ....extract it

That requires having an Organization ... move all from personal.



