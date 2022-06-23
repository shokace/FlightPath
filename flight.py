import requests
import json


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