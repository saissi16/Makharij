import re,sys
p="android/app/src/main/AndroidManifest.xml"
s=open(p,encoding="utf-8").read()
perms=[("android.permission.RECORD_AUDIO"),("android.permission.MODIFY_AUDIO_SETTINGS")]
add=""
for perm in perms:
    if perm not in s:
        add+='    <uses-permission android:name="%s" />\n'%perm
if "android.speech.RecognitionService" not in s:
    add+='    <queries>\n        <intent>\n            <action android:name="android.speech.RecognitionService" />\n        </intent>\n    </queries>\n'
s=s.replace("<application",add+"    <application",1)
open(p,"w",encoding="utf-8").write(s)
print("manifest patched")
