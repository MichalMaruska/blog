---
title: "Syncing reprepro as git"
date: 2024-12-16
draft: true
---

# Syncing reprepro as git

## How to contribute to a debian repository from multiple machines

I use [reprepro](https://wiki.debian.org/DebianRepository/SetupWithReprepro) to build a store of my [debian](https://github.com/MichalMaruska/michalmaruska.github.io) packages. I also started to publish it on [github](https://michalmaruska.github.io/).

Now I want to build arm64 packages on a secondary machine - rpi4. How to do that?

* I keep in [git](https://github.com/MichalMaruska/michalmaruska.github.io)  the **pool**, **dist** and configuration.
* I use "reprepro include  \*.changelog"
* How to merge the work from 2 places?

Reprepro uses a lot of \*.db files to speed up. And there is a lot of state, it's bound to the filesystem, so not shareble (in git).

To merge from the github git repo, I use "reprepro **update**". To sync the rest I should "git merge" but the conflicts are already solved by the "reprepro update" command, so  "dist" should use the "ours" strategy. So

git merge --no-commit

git reset dist

git commit -m .....

To guarantee the sync between those 2 operations a "lease" is needed:

see the [script](https://github.com/MichalMaruska/michalmaruska.github.io/blob/main/git-update)

So, what happens when I build a package ("git") which

* I already build on amd64
* has arm64-specific and also common packages?

debhelper spoils the ... by putting its name in the generated pre/post-install scripts.

This problem is local to  "reprepro include". Let's see:
