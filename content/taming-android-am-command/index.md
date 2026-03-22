---
title: "Taming Android  am command"
date: 2016-11-26
draft: false
---

# Taming Android  am command

In Android an intent can carry data of a certain mime type.
To test this feature, I had an App which sets up an [IntentFilter](https://developer.android.com/reference/android/content/IntentFilter.html), and then I would manually trigger it:

``` sh
> am broadcast -t text/xml -a my.action.START -d "file:///system/usr/share/mmc/settings.xml"
```


It did not work, so I had to read better about [am options](https://developer.android.com/studio/command-line/adb.html#am):

So I learned about `FLAG_DEBUG_LOG_RESOLUTION`(I also saw it in the [sources)](https://github.com/cozybit/aosp-frameworks-base/blob/master/services/java/com/android/server/IntentResolver.java#L207). So I added "-t 8" as option.
Then I saw that the type used during the matching was Null, so I verified the binder transaction code:[reading from binder tx data](https://github.com/android/platform_frameworks_base/blob/master/core/java/android/app/ActivityManagerNative.java#L486) and [writing tx data](https://github.com/android/platform_frameworks_base/blob/master/core/java/android/app/ActivityManagerNative.java#L3495) Here the writing:

``` java
> #### ActivityManagerProxy broadcastIntent().... intent.writeToParcel(data, 0); // serializes the Intent data.writeString(resolvedType); // separately adds the type
```

So the type has to be delivered separately, but **[am](https://github.com/android/platform_frameworks_base/blob/master/cmds/am/src/com/android/commands/am/Am.java#L772)** does not do it:

``` java
> #### private void sendBroadcast() throws Exception
{
Intent intent = makeIntent(UserHandle.USER\_CURRENT);
IntentReceiver receiver = new IntentReceiver();
System.out.println("Broadcasting: " + intent);
// this is the fix null -> intent.getType()
mAm.broadcastIntent(null, intent, /* null */ intent.getType(), receiver, 0,
    null, null, mReceiverPermission, android.app.AppOpsManager.OP\_NONE, true, false, mUserId);
receiver.waitForFinish(); }
```
