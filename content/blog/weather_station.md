Title: Weather Station
Date: 2020-07-18 16:00
Modified: 2022-03-20 05:40
og_image:../images/weather_station/IMG_20200630_170836_edited_1.jpg
Tags: Raspberry Pi, Python, weather station


# As a studied atmospheric scientist it is almost a duty to operate a personal weather station [(PWS)](https://www.wunderground.com/dashboard/pws/IPATSC2/).
Here you can see the outside sensors.
![Photo](/images/weather_station/IMG_20200705_154307_resize.jpg)

Below is a picture of the basis station.
![Photo](/images/weather_station/IMG_20200726_172233_resize.jpg)

It is a [Renkfore WH2315](https://www.amazon.de/Renkforce-WH2315-Funk-WETTERSTATION/dp/B01N4DK6TG#ace-g6772571139) radio weather station.
The station has a radio connection to a basis station and this is connected to a Raspberry Pi.
I used Rasperry Pi OS (32-bit, released 2021-10-30).
Via the open source software [WeeWX](http://weewx.com/) the data is than hosted on [Weather Underground](https://www.wunderground.com/). 

Below you can see a my setting (arrows define the connections).
<img alt="Photo" src="/images/weather_station/setting_without_server.svg">

Here you can see  a sample screenshot of my PWS taken from Weather Underground suitable to the photos above. 
![Photo](/images/weather_station/renkforce_weather_history_ipatsc2_Screenshot from 2020-07-27 21-01-11.png)


## Installation of WeeWX and hosting via Weather Underground:
I followed basically the [WeeWX debian documentation](http://weewx.com/docs/debian.htm). 
```bash
pi@raspberrypi:~ $
wget -qO - https://weewx.com/apt/weewx-python3.list | sudo tee /etc/apt/sources.list.d/weewx.list
sudo apt-get update
sudo apt-get install weewx
```

Because the driver for the Renkforce WH2315 station is not available in WeeWX it has to be installed seperatly see [https://github.com/EdwinGH/weewx-wh23xx/)](https://github.com/EdwinGH/weewx-wh23xx/).
I used than later WH23xx as the driver.


## Status of the weather station:

```bash
pi@raspberrypi:~ $
sudo tail -f /var/log/syslog
```
or

```bash
pi@raspberrypi:~ $
sudo /etc/init.d/weewx status 
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

## Basics of WeeWX:
Configurations are saved here:
```bash
pi@raspberrypi:~ $
/etc/weewx/weewx.conf
```
Quick change / initial setup in weewx.conf:
```bash
pi@raspberrypi:~ $ 
wee_config --reconfigure
wee_config --help
```


Commands:
```bash
pi@raspberrypi:~ $ 
sudo weewxd
sudo /etc/init.d/weewx status
sudo /etc/init.d/weewx restart
sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start
```


Some files are saved here:
```bash
pi@raspberrypi:/var/www/html/weewx $ ls
celestial.html    daytempdew.png   daywind.png         monthhum.png        monthtemp.png     rss.xml            weekhumin.png      weektempin.png   yearbarometer.png  yeartempfeel.png  yearwindvec.png
daybarometer.png  daytempfeel.png  daywindvec.png      monthradiation.png  monthuv.png       seasons.css        weekhum.png        weektemp.png     yearhumin.png      yeartempin.png
dayhumin.png      daytempin.png    favicon.ico         monthrain.png       monthvolt.png     seasons.js         weekradiation.png  weekuv.png       yearhum.png        yeartemp.png
dayhum.png        daytemp.png      font                monthrx.png         monthwinddir.png  statistics.html    weekrain.png       weekvolt.png     yearradiation.png  yearuv.png
dayradiation.png  dayuv.png        index.html          monthtempdew.png    monthwind.png     tabular.html       weekrx.png         weekwinddir.png  yearrain.png       yearvolt.png
dayrain.png       dayvolt.png      monthbarometer.png  monthtempfeel.png   monthwindvec.png  telemetry.html     weektempdew.png    weekwind.png     yearrx.png         yearwinddir.png
dayrx.png         daywinddir.png   monthhumin.png      monthtempin.png     NOAA              weekbarometer.png  weektempfeel.png   weekwindvec.png  yeartempdew.png    yearwind.png
```

## Technical Data (Renkfore WH2315):
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

Finally a link to [live data of my PWS](https://www.wunderground.com/dashboard/pws/IPATSC2/).