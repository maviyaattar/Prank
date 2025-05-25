[app]
title = PrankApp
package.name = prankapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,mp3
version = 1.0
icon.filename = icon.png

requirements = python3,kivy,pyjnius
android.permissions = INTERNET,VIBRATE,WAKE_LOCK,MODIFY_AUDIO_SETTINGS
android.minapi = 21
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1
