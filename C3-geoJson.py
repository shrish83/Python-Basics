import json
import urllib.request, urllib.parse, urllib.error
import ssl

api_key = False
if api_key is False:
    api_key = 42
    base_url = "http://python-data.dr-chuck.net/json?"
else:
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

# University of Athens
place_name = input("Enter a place name: ")

params = dict()
params["address"] = place_name
if api_key is not False: params["key"] = api_key
url = base_url + urllib.parse.urlencode(params)

#address_param = urllib.parse.urlencode({'address': place_name})
#target = base_url + address_param

print ("Retrieving ", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print ("Retrieved ", len(data), "characters")
#print(data)

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

print(json.dumps(js, indent=4))

place_id = js["results"][0]["place_id"]
print("Place id ", place_id)
