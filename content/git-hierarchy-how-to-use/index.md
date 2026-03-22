---
title: "Git-hierarchy  --- how to use"
date: 2012-11-25
draft: false
---

# Git-hierarchy  --- how to use

Documentation on [git-hierarchy](https://github.com/MichalMaruska-TomTom/git-hierarchy).  
  

### Definitions:

Note: when I say branch, I mean the named head.  
  
A "feature branch", or a **segment**, is a triple:  
1/ branch  
2/ *start* commit reference. (points to a real commit - sha1-hash)  
3/ *base* symbolic reference -- name of branch to re-base it on.  
  
A **sum** is a branch name and a list of *summands* -- symbolic references  
of branches, which should be (re-)merged to form the "unique commit" of the branch.  
  
Sums are handy for:  
- the final release commit  
- as the "base" reference for segments.  
  
**poset**: the partial ordering of (relevant) heads, induced by:  
 segment-head **>** the head referenced by the base symref.  
 sum-head **>** each of the heads referenced by the list of summands.  

### Operations:

git-segment  list, describe, create segments, split  
git-sum    list, describe, create, modify  sums  
  
git-rebase-poset the main tool -- rebase/remerge all the sums & segments.  
so that for each segment  *start* is (again) equal to *base*, and sum-heads commits are joins of the summands.  
  
git-rename  .. when renaming branches, rename the whole segment/sum, or  
               update the other symbolic references to reference the changed  name.  
  
git-delete  .. check if possible to delete the sum/segment, or if anything is  
               referencing it -> abort.  

### Implementation:

start ... could have used tags. not now.  
bases ... symbolic references; ex.  ref/base/antiflicker points at "ref: refs/heads/master".  
  
summands ... symbolic refs. ex.  ref/sum/all/1  points at "ref: refs/heads/antiflicker",        ref/sum/all/2 points at "ref: refs/heads/auto-raise ...  
  

### Transferring to other repos

For now it's only a tool for individual use. There are some limitations in Git, which I had to work around:  
  

* "git push" resolves symbolic refs before sending them.
* "git fetch" from GitHub does not fetch refs other than tags & branches.

  
  
So, if I want to at least transfer the structure, I need to patch git, or use this trick:  
  
I can for example make a tag whose message -- as string -- is a table - dump of the symrefs:  
sym-ref-name      ref: .....  
  
git tag "hierarchy-refs" -m "$(git-dump-refs)"  
and on fetching:  
git cat-file tag hierarchy-refs |tail -n +6 |  git-recover-symbolic-refs
