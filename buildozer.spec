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

# Add this to avoid missing dependencies
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 23b
android.archs = armeabi-v7a

# Needed for most modern Android apps
android.gradle_dependencies = androidx.appcompat:appcompat:1.4.1
android.gradle_dependencies = androidx.core:core-ktx:1.7.0

fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1
