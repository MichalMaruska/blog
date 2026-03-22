---
title: "Building pkgsrc with Pbulk"
date: 2020-11-20
draft: true
---

# Building pkgsrc with Pbulk

[Pbulk](http://netbsd.org/docs/pkgsrc/bulk.html) tool is promising, but confusing. I have tried to understand it and at the same time  split it up & adapt to my needs.

## Creating the pbulk too`l`

`mk/pbulk/pbulk.sh`

`This tool does too much to be flexible & explorable. I divided it into the following tools:`

1. `Create the container with bulkbuild tool`
2. `Bootstrap the target pkgsrc installation (*)`
3. `Bind the two with a configuration file`

`Every step must be repeatable, independent.`

## `Building with bulkbuild`

`Some fixes were needed.`

#### `Building in isolation`

`The LOCALBASE is frequently rebuilt, and filled on demand -- nice to use a tmpfs for that.`

`It's nice to keep using pkgsrc while the build runs --- use a separate filesystem/mount namespace:bubblewrap can help here:`

`bwrap --bind / / --dev-bind /dev /dev --tmpfs` `$LOCALBASE  --   $PBULKBASE/bin/bulkbuild  $configdir/pbulk.conf.over`

`(*) In fact the step 2 can also be run inside this bwrap environment.`

#### `Building with pkgsrc compiler`

## `Distributed build`

##
