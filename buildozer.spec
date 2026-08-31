[app]
title = TimeSeriesAnalyticsPlatform
package.name = timeseries_analytics
package.domain = org.timeseries.analytics

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0
requirements = python3,kivy,numpy,pandas

orientation = portrait,landscape
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25.2.9519653
android.archs = arm64-v8a
