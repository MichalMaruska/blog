---
title: "Using github: building on github"
date: 2026-04-27
draft: false
---

# Further steps to deletegate to Github


## I started to build on GH

All I need is build debian packages, and collect them in my repository (reprepro), so
all my machines can seemlessly install them.

### Initial state:
Doing both the package builds and assembling them in a pool on my machines, and exporting the
reprepro (pool, dists) to GH as git, to have it published as gh-pages. But that meant that building
on arm64 (using this local workflow) required its own clone of the reprepro (git repo), and a way to
sync them (maintain the db/ part of reprepro),
and avoid rebuilding arch-independent packages -- unfortunately still not identically --
on both amd64 and arm64.


### Start: let's try to see if it works at all
Lets invoke a build on the gh cloud and push to the reprepro from the workflow! 
Give it GPG key (to sign reprepro), SSH key to access
the central reprepro repository on GH.


### Immediately reprepro is needed.
It should not be pushing the packages, but instead schedule a job on the "apt-repo", which retrieves
the "release artifacts".


### all the satellites -- repositories with debian packages -- repeat the same workflow ....extract it

That requires having an **Organization** ... move all from personal.



### use cache & release  instead of gh-pages branch.
https://github.com/morph027/apt-repo-action  didn't try that


### Old way:
old reprepro: https://github.com/MichalMaruska/michalmaruska.github.io


### New way:
https://github.com/michal-maruska/apt-repo/    main branch with configuration,  gh-pages with the .debs
https://github.com/michal-maruska/workflows  ...shared workflow

satellites, which build on release tag, or manually triggered
https://github.com/orgs/michal-maruska/repositories

resulting apt repository:
https://michal-maruska.github.io/apt-repo/


Publish by Workflow, not by branch (gh-pages).
https://github.com/actions/upload-pages-artifact
