import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# http://py4e-data.dr-chuck.net/comments_944609.json
url = input("Enter location: ")
urlh = urllib.request.urlopen(url)
data = urlh.read()

print("Retrieved", len(data), "Characters")

df = json.loads(data)
df = df["comments"]

Sum = 0

for i in df:
    Sum = Sum + int(i["count"])

print("Sum: ", Sum)