Title: Raspberry Pi Rail Slider
Date: 2020-06-29 21:00
Modified: 2020-07-25 19:30
og_image:../images/PIRailSlider/IMG_20200705_163233_edited_1.jpg
Tags: Raspberry Pi, Python, Time Lapse

# One project I did and currently do is the following.
Here you can see the whole construction at a glance.
![Photo](/images/PIRailSlider/IMG_20200712_115919_compressed.jpg)

Well, what's all this. As you can see, here is a Rasperry Pi (Pi) mounted on a metal sled. 
Basically the camera is pulled along the sled with the help of a motor. I was inspired by the projects of this page [www.DavidHunt.ie](http://www.davidhunt.ie/).

## Construction
![Photo](/images/PIRailSlider/IMG_20200709_191035_resize.jpg)
![Photo](/images/PIRailSlider/IMG_20200709_191045_resize.jpg)

#### What I basically needed for this project
* Pi
* Pi camera
* touchscreen
* 5V powerbank
* wires
* geared 12V DC motor
* belt
* washer for fixing the belt
* 2 iron rods (clothes rails)
* mounting plate
* u-shaped aluminum profile
* ball bearings
* ...

## Code Snippets:
The original code is from James Moore and was edited by me. 
```python
#!/usr/bin/env python
#  raspiLapseCam.py
#
#  Created by James Moore on 28/07/2013.
#  Copyright (c) 2013 Fotosyn. All rights reserved.
#
#  Import some frameworks
from datetime import datetime
import PiRailSlider_f


# Make New folder
new_folder = PiRailSlider_f.mkdir_folder(folder_path='/home/pi/PiRailSlider/LapsePiTouch/Lapse')

#----------------------------------------------
fileSerial = 1

# Run a WHILE Loop of infinitel
while True:
    d = datetime.now()
    print('d:', d)
    if d.hour > 2:
        # rpi-camera
        fileSerial = PiRailSlider_f.raspistill(d=d, fileSerial=fileSerial,
                                          new_folder=new_folder
        )
        fileSerial += 1

        # Starts Motor
        PiRailSlider_f.Motor12V_GPIO_TimeLapse(Motor1A=37, Motor1B=36, Motor1E=33,
                                      t_motor=1, t_sleep=3
        )

    else:

        # Just trapping out the WHILE Statement
        print('=============== Doing nothing at this time')
```
## Youtube Testvideo
[![Minions Banana Song Full Song](http://img.youtube.com/vi/-9EHdp1ynUU/0.jpg)](https://www.youtube.com/watch?v=-9EHdp1ynUU)



#### Will be continued...