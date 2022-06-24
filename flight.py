import sys

import requests
import json
from PIL import Image, ImageDraw

###COORDINATES###
topleft_lat = 90
topleft_long = 180
botright_lat = -90
botright_long = 0


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





with Image.open("map.png") as im:

    image_width, image_height = im.size # this is where things get interesting

    #offsetting x,y grid to fit long + lat coordinates from iss position to fit image
    #x_offset = (float(longitude) - topleft_long) / (botright_long - topleft_long) * image_width #too bad this doesnt work yet
    #x_offset = (float(latitude) - topleft_lat) / (botright_lat - topleft_lat) * image_height


    draw = ImageDraw.Draw(im)
    draw.point((1000,100) + im.size, fill="red")
    im.save("map_point.png") #making initial cross on map.jpg.. testing PIL
    im.show()