#!/usr/bin/env python3

import os, shutil, time, random


while True:
    rand = random.randint(0, 479)
    file_name = "Wallpaper_{}".format(rand)
    cmd = 'gsettings set org.gnome.desktop.background picture-uri file:///home/ironman/Pictures/wallpapers/{}'.format(file_name)
    print('Applying wallpaper', file_name, sep=' : ')
    os.system(cmd)
    time.sleep(300)
