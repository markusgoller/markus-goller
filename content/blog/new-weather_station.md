Title: New Weather Station
Date: 2022-03-23 23:00
og_image:../images/new-weather_station/IMG_20220322_180231.jpg
Tags: Raspberry Pi, Python, weather station

# New Weather Station
Since my old [Renkfore WH2315](https://www.amazon.de/Renkforce-WH2315-Funk-WETTERSTATION/dp/B01N4DK6TG#ace-g6772571139) weather station unfortunately no longer worked properly (connection problems) I had to organize a new one. 
I decided to buy a semi-professional weather station from the provider [dnt](https://www.dnt.de/Produkte/WiFi-Wetterstation-WeatherScreen-PRO/).
The WeatherScreen PRO station is a WiFi weather station, so e.g. you can directly send your data to [Weather Underground](https://www.wunderground.com/), [Ecowitt Weather](https://www.ecowitt.net/), [Weathercloud](https://weathercloud.net/en) or another weather provider.

Here you can see the outside sensors and the basis station:
![Photo](/images/new-weather_station/IMG_20220307_181250_cropped.png)

Below is a picture with the weather station in action.
By the way, the yellow spots are quite valuable dirt (Sahara dust) which was transported from North Africa to Central Europe by a favorable air current at the beginning of March 2022.
![Photo](/images/new-weather_station/IMG_20220322_180242.jpg)

## Changes compared to the old [(Renkforce Weather Station)](https://markusgoller.at/weather-station.html):
A big advantage of the new weather station is  a built-in memory by means of a sd-card.
So if there are connection problems with the station and the WiFi you have no data loss.

Here you can see the new setting:
<img src="/images/new-weather_station/settings_subnails.svg" alt="settings_subnails.svg">
Photo taken from [https://www.netcup.de/](https://www.netcup.de/)


## Publication of the weather station take place in two ways:
* Sending data to Weather Underground automatically 
* Sending data to a private webserver ([Raspberry Pi](https://www.raspberrypi.org/) - [WeeWX](https://www.weewx.com/) - webserver)


### Sending data to Weather Underground automatically:
Only the below setting on the basis station have to be made (sensitive data is marked as XXX)
![Photo](/images/new-weather_station/IMG_20220322_200607_cropped.png)

### Sending private webserver:
First the weather data is send to the Raspberry Pi on which an open source software for weather stations WeeWX is installed. In a second step this data is send to a webserver.
Because the WeatherScreen PRO station has no USB-connection I had to install an extra driver. The driver is available on GitHub via the following link 
[(matthewwall / weewx-interceptor)](https://github.com/matthewwall/weewx-interceptor).
For the installation I followed basically the GitHub documentation and another documenation which is unfortunately only available in German [(https://www.dl1nux.de/erfahrungen-mit-dnt-wetterstation-weatherscreen-pro-und-weewx/)](https://www.dl1nux.de/erfahrungen-mit-dnt-wetterstation-weatherscreen-pro-und-weewx/).

Below is an excerpt of the weewx.conf-file with the settings of the interceptor-driver (192.168.0.164 is the internal IP address of the Pi):
```bash
pi@raspberrypi:~ $ cat /etc/weewx/weewx.conf
##############################################################################

[Interceptor]
    # This section is for the network traffic interceptor driver.
    
    # The driver to use:
    driver = user.interceptor
    
    # Specify the hardware device to capture.  Options include:
    #   acurite-bridge - acurite internet bridge, smarthub, or access
    #   observer - fine offset WH2600/HP1000/HP1003, ambient WS2902
    #   lw30x - oregon scientific LW301/LW302
    #   lacrosse-bridge - lacrosse GW1000U/C84612 internet bridge
    #   ecowitt-client - any hardware that uses the ecowitt protocol
    #   wu-client - any hardware that uses the weather underground protocol
    device_type = ecowitt-client
    port = 40080
    address = 192.168.0.164 

##############################################################################

```



Finally at the basis station a customized server with the Ecowitt protocol has to be installed:
![Photo](/images/new-weather_station/IMG_20220322_200647_cropped.png)



#### Rsync via crontab:
By default, the WeeWX software on the Pi runs with root access. Unfortunately, this also creates all folders as root. In order to store these files on the webserver and make them generally accessible, it is advisable not to grant root access on the server. So in a first step I changed the user of the folder and the group (it is the same user). Then these folders can be copied and stored on the server without any problem with this non-root user.
See also [https://www.pluralsight.com/blog/it-ops/linux-file-permissions](https://www.pluralsight.com/blog/it-ops/linux-file-permissions)

I did everthing via a crontab:
```bash
pi@raspberrypi:~ $ crontab -e

*/1 * * * * sudo chown -R xyuser:xyuser /var/www/html/weewx
*/2 * * * * rsync --numeric-ids -avz /var/www/html/weewx  xyuser@somehost.example.com:/var/www/html 
```

## Finally two links to the weather station:
[webserver (smartphone skin)](http://v2202112116254172535.hotsrv.de/index.html)

[IPATSC5-Wunderground](https://www.wunderground.com/dashboard/pws/IPATSC5)



## Technical Data (WeatherScreen PRO station):
Below is screenshot taken from the [WeatherScreen PRO Data Sheet](https://m.media-amazon.com/images/I/91D93jzNt3L.pdf).
The data sheet  is unfortunately only available in German.
![Photo](/images/new-weather_station/technische_daten_Screenshot_from_2022-03-21 13-57-25.png)