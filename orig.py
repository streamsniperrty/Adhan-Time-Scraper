# Imports
import requests as req
import re
from bs4 import BeautifulSoup as bs
import sys as system

### Web Scraper

# Set URL
# URL = 'https://www.muslimpro.com/Prayer-times-Borough-of-Queens-NY-NY-United-States-5133273'

# User Agent Details
# headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

# The scraper doing its thing

url = "https://www.muslimpro.com/Prayer-times-Borough-of-Queens-NY-NY-United-States-5133273"
r = req.get(url)
soup = bs(r.content, 'html.parser')
soup.prettify()
info = soup.find('tr', {"class": "active"}).get_text()

# Changes output
pattern = re.compile(r'\d')
matches = pattern.finditer(info)

# Each output is now organized as a variable
fajr = info[9:10] + info[10:11] + ":" + info[12:13] + info[13:14]
sunrise = info[14:15] + info[15:16] + ":" + info[17:18] + info[18:19]
dhuhr = info[19:20] + info[20:21] + ":" + info[22:23] + info[23:24]
asr = info[24:25] + info[25:26] + ":" + info[27:28] + info[28:29]
maghrib = info[29:30] + info[30:31] + ":" + info[32:33] + info[33:34]
isha = info[34:35] + info[35:36] + ":" + info[37:38] + info[38:39]

# Finally, each variable is placed into a list
prayertimes = [fajr, sunrise, dhuhr, asr, maghrib, isha]

###

### AdhanBot

# Bot asks you what prayer time you want
# Bot outputs prayer time.

# fajr, sunrise, dhuhr, asr, maghrib, isha, help, all, about
loop = True
while loop == True:
    answer = input("Hello there! Which adhan time would you like to know about? Please type \"HELP\" if your are confused.\n\n")
    print("\n")

    if answer == "about":
        print("AdhanBot 0.1")
        print("Open Source Software, made with Linux")
        print("We use MuslimPro servers to show the times.")
        print("\n")

    elif answer == "HELP":
        print("AdhanBot works by using commands to output adhan times.")
        print("The basic premise is that you type the adhan you want the time for, and AdhanBot will fetch the time for you.")
        print("Commands that are available are: 'fajr', 'sunrise', 'dhuhr', 'asr', 'maghrib', 'isha', 'all', 'HELP', 'about', and 'exit'.")
        print("\n")

    elif answer == "all":
        print("Fajr: " + prayertimes[0])
        print("Dhuhr: " + prayertimes[2])
        print("Asr: " + prayertimes[3])
        print("Maghrib: " + prayertimes[4])
        print("Isha: " + prayertimes[5])
        print("\n")

    elif answer == "fajr":
        print("Fajr: " + prayertimes[0])
        print("\n")

    elif answer == "sunrise":
        print("Sunrise: " + prayertimes[1])
        print("\n")

    elif answer == "dhuhr":
        print("Dhuhr: " + prayertimes[2])
        print("\n")

    elif answer == "asr":
        print("Asr: " + prayertimes[3])
        print("\n")

    elif answer == "maghrib":
        print("Maghrib: " + prayertimes[4])
        print("\n")

    elif answer == "isha":
        print("Isha: " + prayertimes[5])
        print("\n")

    elif answer == "exit":
        print("Exiting AdhanBot...\n")
        system.exit()
