import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter location: ")

urlh = urllib.request.urlopen(url)
data = urlh.read()
#print('Retrieved',len(data),'characters')
#data = data.decode()
#print(data)

# http://py4e-data.dr-chuck.net/comments_944608.xml
treeList = ET.fromstring(data)
counts = treeList.findall(".//count")   ###<count> tags
print("Counts: " + str(len(counts)))

acc = 0
for count in counts:
    acc = acc + int(count.text)

print("Sum is " + str(acc))