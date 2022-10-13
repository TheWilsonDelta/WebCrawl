import os
import time
import webbrowser

import requests
from bs4 import BeautifulSoup

OpenedArray = []

url = "https://carbonite.co.za/index.php?forums/32.rss"
#url = "https://carbonite.co.za/index.php?forums/32/"

resp = requests.get(url)
soup = BeautifulSoup(resp.content, features="xml")

#mydivs = soup.findAll("div", {"class": "structItem-title"}).findParent()

items = soup.findAll('item')
#print(soup.prettify())

for item in items:
    text_file = open("mydata.txt", "a")
    text_file.writelines(item.title.text + "\n")
    text_file.close()
print("Adding new form adverts")

x = 0
while x < 10000000000:

    text_file = open("mydata.txt", "r")
    Array = text_file.readlines()
    for sub in Array:
        OpenedArray.append(sub.replace("\n", ""))
    text_file.close()

    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features="xml")

    items = soup.findAll('item')
    item = items[0]

    BodyText = str(item.encoded.text)
    Wanted = "Desired Age" in BodyText
    Reseller = "Reseller" in BodyText

    if item.title.text not in OpenedArray and Wanted is False and Reseller is False:
        text_file = open("mydata.txt", "a")
        text_file.writelines(item.title.text + "\n")
        text_file.close()
        print("Added New Entry")
        webbrowser.open(item.link.text, new=2)
        os.system('play -nq -t alsa synth {} sine {}'.format(1, 600))
    else:
        print("Nothing New")

    time.sleep(20)
    x += 1
