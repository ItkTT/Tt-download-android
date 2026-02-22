[app]
title = TT Ultimate Pro
package.name = ttdownloader
package.domain = org.itktt
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,flask,yt-dlp,requests
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
# force update
