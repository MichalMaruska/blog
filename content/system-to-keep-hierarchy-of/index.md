---
title: "System to keep a hierarchy of modifications for public software."
date: 2012-10-12
draft: false
---

# System to keep a hierarchy of modifications for public software.

## System to keep a hierarchy of modifications for public software.

  
I have developed a few extensions to free/open software, over past years.  
  
Doing so in spare time, my priority was to get the features done,  
at the cost of code quality, sharing(?).  
  
During years, naturally, a need arose to re-apply those big patches to  
evolving upstream sources.  
  
So, inspired by Debian, I started to experiment with *Quilt*, and  
represented my modifications as progressions of patches.  
  
  
  
But there were certain projects, where my changes were so big,  
that I was not able to extract such a linear sequence without  
additional tools.  
  
With the help of Git and especially *Magit*, I started to  
classify separate diff hunks, then group those classified as related  
and regroup etc.  
  
  (I did this for my changes to Sawfish WM).  
  
The whole set of changes grew to be  layers of changes, some dependent  
on previous ones;  not a previous one, but more of them.  
  
  
So I wanted to understand this partial ordering, and somehow represent it in Git.  
  
The benefit for this would be easier future rebasing upon new upstream,  
since rebasing smaller parts requires  less knowledge (decisions) at a time. And  
some of my features can be also implemented upstream -- so I can just drop that  
part of my changes, and  adapt/rework the rest.  
  
  
Single "features" are thus represented as a linear sequence of commits,  
and the dependency between them is represented by "basing" one  "feature"  
on  a merge (commit) of  prerequisite features.  
  
  
So, in my current version, I have merges - "sums", which are just lists  
of features - "segments". And "segments" are "branches"  with  
a Start commit (a hash id), and a symbolic "base", which is a "sum".  
That base-sum can also be a trivial sum -- a simple  segment.  
  
Rebasing such a hierarchy is a matter of walking in the topological order of  
the dependency (between features -- segments) and sums,  
rebasing them --onto the updated "bases"  or  redoing merges.  
  
  
  
[Code is here](https://github.com/mmaruska/git-hierarchy)
