import sys

import requests
import json
import math
import numpy as np
from PIL import Image, ImageDraw

###COORDINATES###
topleft_lat = 90
topleft_long = 180
botright_lat = -90
botright_long = 0

###MATH###
rad_earth = 6371 #radius earth km

r = requests.get('http://api.open-notify.org/iss-now.json')

if (r.status_code > 200):
    print("status code: " + r.status_code)
    exit()
else:
    print("connection successful")

longitude = ""
latitude = ""


rawData = json.loads(r.text)
for data in rawData['iss_position']['longitude']:
    longitude += data
for data in rawData['iss_position']['latitude']:
    latitude += data

print("longitude: " + longitude)
print("latitude: " + latitude)


##BACKGROUND IMAGE INITIALIZATION##

bg = Image.open("map.png")
image_width, image_height = bg.size

def get_cartesian(lat=None,lon=None):
    lat, lon = np.deg2rad(lat), np.deg2rad(lon)
    x = rad_earth * np.cos(lat) * np.cos(lon)
    y = rad_earth * np.cos(lat) * np.sin(lon)
    return x,y


xy = get_cartesian(float(latitude),float(longitude))

print(xy)
x = int(((xy[0])+6371)/(rad_earth/image_width))
y = int(((xy[1])+6371)/(rad_earth/image_height))
print(x,y)


##ISS ICON INITIALIZATION## 3444228.8365710177

icon = Image.open("iss.png")
bg.paste(icon, (x,y), mask = icon.im)






bg.show()






