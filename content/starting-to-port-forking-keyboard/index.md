---
title: "Starting to port Forking keyboard driver to Windows"
date: 2024-11-11
draft: false
---

# Starting to port Forking keyboard driver to Windows

# Introduction

 After 20 years of developing a "forking" keyboard driver for Xfree86/Xorg, I decided to finally attempt to make it available on Windows.

 As a first step I split the code into portable core, and the interfacing glue for Xorg.  [In a couple of days](https://github.com/MichalMaruska/fork-plugin/blob/master/doc/porting-to-weston.md) I implemented such a [glue](https://github.com/MichalMaruska/fork-plugin/tree/master/libinput) for the "libinput" to be used in Weston (Wayland).

# Plan for Windows

Encouraged by the speedy adaptation, I started to assemble the tools for Windows:

1. [wdk](https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk)
2. [visual studio](https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk)
3. a "target" machine (KVM+Qemu  running Windows).

Requirements for 3. included public IP for the guest VM ([ping](https://community.fortinet.com/t5/FortiGate/Troubleshooting-Tip-Window-10-computer-does-not-reply-to-ping/ta-p/286927) should be possible).

virt-install --name win11 --cdrom Win11\_24H2\_EnglishInternational\_x64.iso 

virt-viewer win11

## Host machine setup

Installing VS was easy, and included a misleadingly named "wdk-extension" which did **not** include WDK itself. So  ntddk.h header was *missing* during the first builds.      Installing WDK properly solved that.

## Target machine

Regarding  [preparation](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/provision-a-target-computer-wdk-8-1) ... just re-read and execute correctly the steps.

I didn't install any SDK or VStudio on the target PC! Only the WDK.

For "non-enhanced mode" ....I didn't do anything with my KVM/Qemu setup.

WDK Test Target Setup MSI ... indeed provided by WDK. (If by chance you install SDK, you will find other MSI files but those are irrelevant.)

**Provisioning** made inside VS (on the host) ... sometimes fails. Repeating can fix it.

This create the WDKRemoteUser account (on the target) and logs as it. On one physical machine I couldn't login as it has an unknown password.

## Deploying

I started to try-out [Sample drivers](https://github.com/Microsoft/Windows-driver-samples). In particular the [kbfilter](https://github.com/microsoft/Windows-driver-samples/tree/main/input/kbfiltr). Deploy **failed**.

* one can see the XML logs... one has to understand that  "Driver Test Group Explorer" tab is sibling of "Git Changes" and "Solution Explorer".
* Or you can make a video of the terminals opened on the target -- they disappear quickly.

The message is the same in both "Cannot create a stable subkey under a volatile parent key". Other failures could be present too.

So re-read the [Readme](https://github.com/microsoft/Windows-driver-samples/blob/main/input/kbfiltr/README.md) and the [INF file template](https://github.com/microsoft/Windows-driver-samples/blob/main/input/kbfiltr/sys/kbfiltr.inx)

- Set the hardware ID in the inx file

I didn't see any

> WdfCoinstaller010xx.dll
The coinstaller for version 1.xx of KMDF.

## Manual build

Using MSBuild ... does work, but does not help with the deployment.

## Manual deployment

So, while searching for solutions of the aforementioned issues I learned:

\* [dbgview](https://learn.microsoft.com/en-us/sysinternals/downloads/debugview)  seems similar to dmesg of linux. But it crashes sometimes (disappears). How to see messages during the boot?  
To see kernel message it must be run "as administrator" !

\* [devcon](https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/devcon-install) tool -- mysterious tool installed during the provisioning (by VS)

https://github.com/hawku/TabletDriver/issues/225

I looked at the github issues of the sample drivers -- for example:

about [devcon install](https://github.com/microsoft/Windows-driver-samples/issues/198).

\* regedit  .... indeed ... there is a key which is **crucial**:

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E96B-E325-11CE-BFC1-08002BE10318}\UpperFilters](https://learn.microsoft.com/en-us/samples/microsoft/windows-driver-samples/keyboard-input-wdf-filter-driver-kbfiltr/)

But beware .... the format *while editing* is ..... one item per line

"kbdclass kbfilter" .... this indeed makes it work !!!

Wrong value and you lose keyboard !!!!!

\* devmgr one can observe, manually remove.

# So, what works?

deploy (from VS). Then  just "Update" the driver of the PS/2 keyboard device...

if it says "Already up-to-date" then your HW-id is wrong!!! So update the \*inf with correct value.

and Registry -- irrelevant.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjagGvinhDiMiy2E-suKtC85jQPpr1AjsBTUddvSBu2a4h6Yi8fj8l-dduZ6f-aQpA5-JIme58C-zcvQIOwidbAlXKFboHdw1r-WLzS0izjcB-M0gABIOdfnLRlcxIxloJoXrIM11WJaNybCn1_MHqi7TS12wPJv4UIcZ5rjfXb58F7Ju7OKJBWNmK7wBg/w648-h352/working-kbfiltr.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjagGvinhDiMiy2E-suKtC85jQPpr1AjsBTUddvSBu2a4h6Yi8fj8l-dduZ6f-aQpA5-JIme58C-zcvQIOwidbAlXKFboHdw1r-WLzS0izjcB-M0gABIOdfnLRlcxIxloJoXrIM11WJaNybCn1_MHqi7TS12wPJv4UIcZ5rjfXb58F7Ju7OKJBWNmK7wBg/s2007/working-kbfiltr.png)

  

WdfDriverCreate [was failing with 0xC000009A](https://stackoverflow.com/questions/38231468/kmdf-wdfdrivercreate-function-returns-insufficient-resources) so disable the verification.
