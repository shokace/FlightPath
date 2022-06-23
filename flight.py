import sys

import requests
import json
from PIL import Image, ImageDraw

r = requests.get('http://api.open-notify.org/iss-now.json')

if (r.status_code > 200):
    print("status code: " + r.status_code)
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

with Image.open("../FlightPath/map.jpg") as im:

    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)

    # write to stdout
    im.save(sys.stdout, "PNG") #making initial cross on map.jpg.. testing PIL