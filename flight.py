import requests
import json
from PIL import Image, ImageDraw

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



x = int((image_width/360) * (180 + float(longitude)))
y = int((image_height/180) * (90 - float(latitude)))


##ISS ICON INITIALIZATION## 3444228.8365710177

icon = Image.open("iss.png")
bg.paste(icon, (x,y), mask = icon.im)






bg.show()






