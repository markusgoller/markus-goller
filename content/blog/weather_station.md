Title: Weather Station
Date: 2020-07-18 16:00
Modified: 2020-11-15 20:00
og_image:../images/weather_station/IMG_20200630_170836_edited_1.jpg
Tags: Raspberry Pi, Python, weather station

# As a studied atmospheric scientist it is almost a duty to operate a personal weather station [(PWS)](https://www.wunderground.com/dashboard/pws/IPATSC2/).

Here you can see the outside sensors.
![Photo](/images/weather_station/IMG_20200705_154307_resize.jpg)

It is a Renkfore radio weather station ["WH2315"](https://www.amazon.de/Renkforce-WH2315-Funk-WETTERSTATION/dp/B01N4DK6TG#ace-g6772571139).
The station has a radio connection to a basis station and this is connected to a Raspberry Pi.
The data is than hosted via [WeeWX](http://www.weewx.com/) to [Weather Underground](https://www.wunderground.com/).

Below is a picture of the basis station.
![Photo](/images/weather_station/IMG_20200726_172233_resize.jpg)

Here you can see a sample screenshot of my PWS taken from Weather Underground suitable to the photo above. 
![Photo](/images/weather_station/renkforce_weather_history_ipatsc2_Screenshot from 2020-07-27 21-01-11.png)

## Technical Data:
|                       |                       | Range                  | Resolution                                                                 | Accuracy                                                          |
|-----------------------|-----------------------|------------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------|
| Basis Station sensors |                       |                        |                                                                            |                                                                   |
|                       | Temperature           | -9.9 °C - +60 °C       | 0.1%                                                                       | +-1 °C                                                            |
|                       | Relative humidity     | 1% - 99%               | 1%                                                                         | +-5%                                                              |
|                       | Barometric pressure   | 300 - 1100 hPa         | 0.1%                                                                       | +-3 hPa in the area of 700 - 1100 hPa                             |
| Outside sensors       |                       |                        |                                                                            |                                                                   |
|                       | Temperature           | -40 °C - +60 °C        | 0.1 °C                                                                     | +-1 °C                                                            |
|                       | Relative humidity     | 1% - 99%               | 1%                                                                         | +-5%                                                              |
|                       | Rain volume           | 0 - 9999 mm            | 0.3 mm (at rain volume of < 1000 mm) 1 mm (at rain volume of >= 1000 mm)   | +-10%                                                             |
|                       | Wind speed            | 0 - 50 m/s             | -                                                                          | +- 1 m/s  (at wind speed < 5 m/s) +- 10% (at wind speed >= 5 m/s) |
|                       | Illumination strength | 0 - 300000 lux         | -                                                                          | +- 15%                                                            |
|                       | UV-index              | 0 - 15 (0 - 20000 W/m² | -                                                                          | -                                                                 |


## Status of the weather station called via the Pi:
```
pi@raspberrypi:~ $ sudo /etc/init.d/weewx status 
● weewx.service - LSB: weewx weather system
   Loaded: loaded (/etc/init.d/weewx; generated; vendor preset: enabled)
   Active: active (running) since Sun 2020-11-15 14:21:41 CET; 52min ago
     Docs: man:systemd-sysv-generator(8)
  Process: 612 ExecStop=/etc/init.d/weewx stop (code=exited, status=0/SUCCESS)
  Process: 714 ExecStart=/etc/init.d/weewx start (code=exited, status=0/SUCCESS)
   CGroup: /system.slice/weewx.service
           └─729 python /usr/bin/weewxd --daemon --pidfile=/var/run/weewx.pid /etc/weewx/weewx.conf

Nov 15 15:05:19 raspberrypi weewx[729]: restx: Wunderground-PWS: Published record 2020-11-15 15:05:00 CET (1605449100)
Nov 15 15:05:32 raspberrypi weewx[729]: cheetahgenerator: Generated 8 files for report SeasonsReport in 12.61 seconds
Nov 15 15:05:38 raspberrypi weewx[729]: imagegenerator: Generated 14 images for SeasonsReport in 6.01 seconds
Nov 15 15:05:38 raspberrypi weewx[729]: copygenerator: copied 0 files to /var/www/html/weewx
Nov 15 15:10:30 raspberrypi weewx[729]: manager: Added record 2020-11-15 15:10:00 CET (1605449400) to database 'weewx.sdb'
Nov 15 15:10:30 raspberrypi weewx[729]: manager: Added record 2020-11-15 15:10:00 CET (1605449400) to daily summary in 'weewx.sdb'
Nov 15 15:10:31 raspberrypi weewx[729]: restx: Wunderground-PWS: Published record 2020-11-15 15:10:00 CET (1605449400)
Nov 15 15:10:44 raspberrypi weewx[729]: cheetahgenerator: Generated 8 files for report SeasonsReport in 12.67 seconds
Nov 15 15:10:50 raspberrypi weewx[729]: imagegenerator: Generated 14 images for SeasonsReport in 5.98 seconds
Nov 15 15:10:50 raspberrypi weewx[729]: copygenerator: copied 0 files to /var/www/html/weewx
pi@raspberrypi:~ $ 
```

## Stop / Start the connection to the Pi (in case of errors):
```
pi@raspberrypi:~ $ sudo /etc/init.d/weewx stop
```
```
pi@raspberrypi:~ $ sudo /etc/init.d/weewx start
```



Finally a link to [live data of my PWS](https://www.wunderground.com/dashboard/pws/IPATSC2/).

### Will be be continued...