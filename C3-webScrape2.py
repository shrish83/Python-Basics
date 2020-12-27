# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url:  http://py4e-data.dr-chuck.net/known_by_Haydon.html
# count: 7
# pos: 18
url = input('Enter - ')
count = int(input("Enter repeating count - "))
pos = int(input("Enter position - "))

names = []

while count > 0:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    anchor = soup("a")
    name = anchor[pos - 1].string
    #print(name)
    names.append(name)
    #print(names)
    url = anchor[pos-1]["href"]
    #print(url)
    count = count - 1

print(names[-1])
