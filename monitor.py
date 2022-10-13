import os
import time
import webbrowser

import requests
from bs4 import BeautifulSoup

OpenedArray = []

url = "https://carbonite.co.za/index.php?forums/9/index.rss"

resp = requests.get(url)
soup = BeautifulSoup(resp.content, features="xml")

items = soup.findAll('item')

for item in items:
    text_file = open("monitor.txt", "a")
    #text_file.writelines(item.title.text + "\n")
    text_file.close()
print("Adding new form adverts")

x = 0
while x < 10000000000:

    text_file = open("monitor.txt", "r")
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

    #OpenedArray = list(dict.fromkeys(OpenedArray))

    if item.title.text not in OpenedArray and Wanted is False and Reseller is False:
        text_file = open("monitor.txt", "a")
        text_file.writelines(item.title.text + "\n")
        text_file.close()
        print("Added New Entry")
        webbrowser.open(item.link.text, new=2)
        duration = 1
        freq = 440
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    else:
        print("Nothing New")

    #lines_seen = set()
    #outfile = open("mydata.txt", "w")
    #for line in open("initialdata.txt", "r"):
    #    if line not in lines_seen:
    #        outfile.write(line)
    #        lines_seen.add(line)
    #outfile.close()

    time.sleep(20)
    x += 1
