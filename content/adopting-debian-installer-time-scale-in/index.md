---
title: "Story of abandoning own tool in favour of learning multiple projects and combining them"
date: 2023-09-04
draft: false
---

# Story of abandoning own tool in favour of learning multiple projects and combining them

# Adopting Debian Installer  (time scale)

In 2016 I started to formalize the way I want to replicate my debian installation on other PCs. I think I needed that once per year.

That is indicated by git commits of a repo with numbered scripts -- stages of installing debian & my expected packages & modifications, after booting with a usb flash drive.

Disk-partitioning was hard (shrinking Windows partitions), configuring apt also forever evolving.

Prior to that I would have just reattach the disks and copied the filesystem.

After 6 years, in 2022 (having used those tools about 10 times) I started to suspect I could spend my time better by learning & fixing a publicly developed tool.

And indeed in April 2023 I tried out the [debian-installer](https://www.debian.org/releases/stable/amd64/index.en.html) (the "hd-media" option), with some pre-seeding.

Then I needed more than pre-seed & targeting *unstable*/SID: I wanted to understand all possible disk encryption setups, and using my additional [apt repository](https://github.com/MichalMaruska-TomTom/michalmaruska-tomtom.github.io) (+ apt configuration).

## Experiments

So, I was using the build system in [debian-installer](https://salsa.debian.org/installer-team/debian-installer.git) (to build customizations) and decided to use a virtual PC (KVM-qemu) to quickly test the result.

I had to overcome [bug 940801](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=940801)

I could test the partitioning with encryption on a virtual disk (10GB).

* Started to wonder about having "udeb" packages in my reprepro.
* Not really sure what is inside "mini.iso", maybe all is inside the initrd?

## 

## 

### Setting up PXE

I wanted to also avoid using flash drives/sd-cards  -- using PXE seems more elegant. Also using netboot rather than hd-media seems a nice simplification.

But there's a catch: this requires modifying DHCP server (which I cannot do on my main modem/route), and I didn't want to set a separate dhcp just for this use-case (on a linux box, with the only connection to the booting PC).

Anyway, I started still with KVM -- a new "bridge" with dhcp pointing at local tftp.

I had to use signed grub to boot with secure-boot.

### Going for physical PC

So I installed **dd-wrt** on another router/wifi access point, and detached from its "bridge" between all LAN connectors one connector which is then serviced by a new dhcp server, and advertises the necessary option for PXE boot.

## First successful run

I included a custom udeb: I needed a modified "[choose-mirror](https://salsa.debian.org/installer-team/choose-mirror.git)" to debug still flaky pre-seed configuration of the net interface.

Partitioning seems intuitive (once you want to use the same key for both Swap & Root fs).

Choose the minimal (ssh server, standard), and after the reboot  do still some manual copying, apt configuration, and finally install my  "[top](https://github.com/MichalMaruska-TomTom/maruska-top)" virtual packages.
