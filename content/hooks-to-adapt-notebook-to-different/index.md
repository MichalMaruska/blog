---
title: "Hooks to adapt a notebook to different conditions"
date: 2013-10-09
draft: false
---

# Hooks to adapt a notebook to different conditions

So, I use Ubuntu 12.04 on my notebook.  
  
Here a list of (shell) hooks I implemented to make the system adapt to "the environment". Only the minimum relevant code  
  

* Open/close lid -> internal screen on/off  
  /etc/acpi/local/lid.sh.pre  
  DISPLAY=:0
grep -q closed /proc/acpi/button/lid/\*/state  
xrandr -display $DISPLAY --output $internal --off  

* When (un)docked -> external monitor on/off.  un/docking detected by AC online. No other way found (with Dell latitude e\*)  
    
  /etc/acpi/power.sh  
    
  if [ $(cat /sys/class/power\_supply/AC/online) = "1" ]; then  
  DISPLAY=:0 xrandr --output DP-1 --auto --rotate left
* Turn audio off/on  when on office network/at home:  
  /etc/dhcp/dhclient-enter-hooks.d/  does not work with NM (see <https://bugzilla.gnome.org/show_bug.cgi?id=709247> )  
  So /etc/network/if-up.d/mute-in-office  
    
   if [ ${DHCP4\_DOMAIN\_NAME-} = 'domain.name' ];  
     amixer set Master mute  
   elif [ ${CONNECTION\_ID-} = "home-ssid" ];  
          amixer set Master unmute  
          amixer set Front unmute  
          amixer set Headphone unmute
* prevent Skype from animating (in gnome-panel) when offline  
  skype without any dbus  access?  
    
  /etc/network/if-post-down.d/stop-skype  
  sleep 10s  
  killall -STOP skype  
    
  /etc/network/if-up.d/resume-skype  
  killall -CONT skype
* keep cpu at minimum  
  /etc/pm/sleep.d/20-cpuspeed  
  case "$1" in  
          resume | thaw)  
  sudo cpufreq-set --governor powersave  
  foreach dir (/sys/devices/system/cpu/cpu\*/cpufreq/) {  
     echo powersave | sudo tee $dir/scaling\_governor  
     echo 1199000 | sudo tee $dir/scaling\_min\_freq  
  ...  
  #sudo hdparm -Y /dev/sdb
