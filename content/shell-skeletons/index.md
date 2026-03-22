---
title: "Shell skeletons"
date: 2013-05-17
draft: false
---

# Shell skeletons

## Shell skeletons --- a tool to start using a sequence of commands

  
When I started to build debian packages from Git, I adopted [git-buildpackage](http://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html).  
The steps I used were (at least) 7:  
  
  

* git-dch  --release "--debian-tag=michal/%(version)s"
* git add debian/changelog;
* git commit -m release
* git-buildpackage --git-tag "--git-debian-tag=michal/%(version)s"
* debi --debs-dir ../build-area/
* git-buildpackage -S
* debrelease -S  --debs-dir=../build-area --dput

  
  
I had this recipe in a file/editor, and pasted line by line into shell, possibly adapting the text, and then invoked.  
In case of error I could reinvoke the command, with some modification.  
  
Then I learned that with Zsh, I can programmatically use that feature which implements C-q (push-line):  there is a stack which I can pre-populate, and then  
ZLE will  prefill the command line by popping the strings from the stack.  
  
So I came up with this function:  
``` zsh
zload-file () {  
        file=$1  
        setopt nomonitor  
        coproc tac $file &|  
        while read line  
        do  
                builtin print -z $line  
        done <&p  
        wait  
        setopt monitor  
}  
```
Sure, I have to put the lines in reverser order -- the last one to be pushed as first, so that it ends at the bottom.

PS: After a while I learned/realized all the arguments of those commands, and made scripts (release & snapshot) which hide all the details, and expose different set of options-- those which I care about.
