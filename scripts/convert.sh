#!/usr/bin/zsh -feu

# Given result of ./blogger_to_md.py, reorganize:
# out/date-dir -> content/dir
# drop the date- part

# must be invoked inside out/

DEST=../content/


foreach dir (*(/)) {
    date=${dir:0:10}
    name=${dir:11}

    mv -v $dir $DEST/$name
    echo "* $date [$name]($name/index.md)"
} > $DEST/index.md
