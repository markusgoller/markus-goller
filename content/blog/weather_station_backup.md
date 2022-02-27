Title: Weather Station Backup
Date: 2022-02-16 13:00
og_image:../images/weather_station/IMG_20200630_170836_edited_1.jpg
Tags: Raspberry Pi, weather station

# Weather Station Backup:
Backup for the [WeeWX](http://www.weewx.com/)-configuration of the Renkfore WH2315 radio weather station:
A detailed description can be seen in the main article [(Weather Station)](https://markus-site.at/weather-station.html).
Docs have been taken from the [WeeWX docs-site](http://weewx.com/docs/usersguide.htm#backup).


# The following files and folders have to be copied: 
* Configurations (/etc/weewx/weewx.conf)
* Skins and templates (/etc/weewx/skins)
* Custom code or extensions (/usr/share/weewx/user)
* Database (/var/lib/weewx/weewx.sdb)  ...do not make a copy of the SQLite database between in the middle of a transaction!


# Restore from backup:
Install WeeWX and replace the default files with those from above.
