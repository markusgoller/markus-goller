Title: Pi as Server
Date: 2022-02-16 16:00
og_image:../images/weather_station/IMG_20200630_170836_edited_1.jpg
Tags: Raspberry Pi, weather station


# Pi as Server
In order to publish the data of my [Renkfore WH2315](https://www.amazon.de/Renkforce-WH2315-Funk-WETTERSTATION/dp/B01N4DK6TG#ace-g6772571139) radio weather station elsewhere as on [Weather Underground](https://www.wunderground.com/) an external server has to be installed.
I have bought a vServer on [netcup](https://www.netcup.de/). 
This server workes with [nginx](http://nginx.org/) as webserver.

Here you can see my setting (arrows define the connections).
<img src="/images/pi_as_server/setting_with_server.svg" alt="setting_with_server">

A detailed description can be seen in the main article [(Weather Station)](https://markusgoller.at/weather-station.html).


## Installation takes place on the Pi and on the server:
Following links give good overviews:
[How to Install Nginx on Raspberry Pi (Tony Teaches Tech)](https://tonyteaches.tech/nginx-raspberry-pi/) with including [video](https://www.youtube.com/watch?v=ECsQ8jbpMow&t=35s).

First I have installed nginx:
```bash
pi@raspberrypi:~ $
sudo apt update
sudo apt upgrade
sudo apt install nginx
```

## I have basically worked through the following steps in the [WeeWX](http://weewx.com/docs/usersguide.htm#integrating_with_webserver) documentation:
Verify that nginx is running:
```bash
pi@raspberrypi:~ $
systemctl status nginx
```

WeeWx does host the files here:
```
pi@raspberrypi:~ $ ls /var/www/html/
index.nginx-debian.html  weewx
```

So Nginx should contain the following configuration:
```bash
pi@raspberrypi:~ $ vim /etc/nginx/sites-available/default
...
# include snippets/snakeoil.conf;

root /var/www/html;

...
```

Test that nginx runs on local network:
```
http://192.168.0.115/index.nginx-debian.html
```
![Photo](/images/pi_as_server/index_nginx-debian_html.png)

```
http://192.168.0.115/weewx/index.html
```
![Photo](/images/pi_as_server/weewx_index.png)

### [Commands]((https://www.cyberciti.biz/faq/nginx-restart-ubuntu-linux-command/)):
```bash
pi@raspberrypi:~ $
sudo systemctl start nginx 
sudo systemctl stop nginx 
sudo systemctl restart nginx
```

### Integrating the webserver:
To publish the data of weewx and make finally worldwide available over the Internet the 
```
/var/www/html/weewx  
```
folder has only to be synced via a cronjob.


