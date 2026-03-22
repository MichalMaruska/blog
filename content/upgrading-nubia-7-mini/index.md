---
title: "Upgrading Nubia 7 mini"
date: 2017-05-29
draft: false
---

# Upgrading Nubia 7 mini

I recently bought this  phone on [marktplaats](http://www.marktplaats.nl/), already upgraded to Mokee Android 7. I liked the features, my previous phone used Android 4.2.  
So I bought another one for my wife, this time I had to make the upgrade myself. It was not straightforward:  
  
The first nubia used as recovery  TWRP 3.0.2-0, the other is with clockwork-mod (v6.0.5.0).  

* I had to resize the big "grow" partition manually, i.e. merge it with "userdata".
* suddenly I saw disconnections of Wifi, and that was due to the same MAC address of the 2 nubias.

### MAC address

So I searched for a solution to tune the MAC address. I found the hint on Intf0MacAddress in WCNSS\_qcom\_cfg.ini. But it did not work.

> /data/misc/wifi/WCNSS\_qcom\_cfg.ini  nor  /system/etc/wifi/WCNSS\_qcom\_cfg.ini

So I had a workaround to  
> echo 98:6c:f5:63:ec:d0 > /sys/devices/fb000000.qcom,wcnss-wlan/wcnss\_mac\_addr

while in airplane mode.  
In the end I  found /persist/WCNSS\_qcom\_cfg.ini which indeed works, and overrides the other 2 files.  
  

### ANDROID\_SERIAL to distinguish them?

To have them accessible via adb at the same time, I need to distinguish by this serial number, which is unfortunately identical. For now I overwrite the kernel cmdline in img\_info with "androidboot.serialno=XXX"  

### Proximity sensor

After receiving some (whatsapp) calls, I noticed it was almost impossible to get the screen back on, as expected.

So, as a workaround I turned off  in Phone> Settings> Accessibility> Use proximity sensor.

But Whatsapp does not seem to have this option.

So I installed [Sensors test](https://play.google.com/store/apps/details?id=asd.vector.sensor&hl=en) and some app to "reset/calibrate" but to no effect.

So I started to look for the kernel driver, to fix a possible bug. There are confusingly multiple kernel sources on github:

1. <https://github.com/nx507j-dev/android_kernel_nubia_nx507j>
2. <https://github.com/ztemt/NX507J_5.1_kernel>
3. <https://github.com/MoKee/android_kernel_nubia_nx507j.git>
4. <https://github.com/MoKee/android_kernel_zte_nx507j.git>

The 3rd is the one used on Mokee (my fixes in <https://github.com/mmaruska/android_kernel_nubia_nx507j>). The other ones fail when (Android) "init" configures (selinux) sepolicy.

Btw. failures of the other kernels can be seen thanks to android ram-console: after the failure, the phone reboots to recovery and

> adb shell cat /proc/last\_kmsg

shows the problem.

In the end the problems is only the calibration, so

>  echo 500 > prox\_threshold\_low

fixes the issue. To see this value, I did:

> cd /sys/class/proximity/proximity/  
> echo 1 > prox\_debug

and "dmesg -c" while running the sensor test app, to see:

> [43580.286869] [SENSOR\_ALS\_PROX] [taos\_prox\_threshold\_set: 2338] proxdata = 396

I guess it's stored in /persist/proxdata/threshold ?  
  
  

### Other issues

  

#### calendar/alarm database -- crash when entering the Alarm app:

> android.database.sqlite.SQLiteException: Can't downgrade database from version 12 to 8

  
I removed the relevant file.  
  

#### SystemUI crash due to wallpaper using too big image

  
> java.lang.RuntimeException: Canvas: trying to draw too large(143769600bytes) bitmap.  
> ....  
> AppCrashReceiver: com.android.systemui stopped unexpectedly...

  
rm  /data/system/user/0/wallpaper\_\*  
  
  
  
My improvements (divided into feature-segments) <https://github.com/mmaruska/android_kernel_nubia_nx507j/network>
