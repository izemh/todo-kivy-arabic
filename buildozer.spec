
[app]
title = ToDoList
package.name = todolist
package.domain = org.zamhor
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0
orientation = portrait
fullscreen = 1

requirements = kivy,kivym
android.permissions = INTERNET

android.archs = armeabi-v7a, arm64-v8a
android.minapi = 21
android.sdk = 30
android.ndk = 23b

[buildozer]
log_level = 2
warn_on_root = 1
