from bs4 import BeautifulSoup as bs
import requests
from datetime import date as d
import sys

# Install bs4, requests

### TODAYS DATE
day = d.today()
date = day.strftime("%a %b %d")

### WEB SCRAPING AND TIME STORAGE

# Parse Website
url = "https://www.muslimpro.com/Prayer-times-Borough-of-Queens-NY-NY-United-States-5133273"
r = requests.get(url)
soup = bs(r.content, 'html.parser')
soup.prettify()

today = soup.find("tr", class_="active")

def prayer(whichTime):
    # fajr, dhuhr, asr, maghrib, isha
    prayerTimes = [today.findChildren()[1].text, today.findChildren()[3].text, today.findChildren()[4].text, today.findChildren()[5].text, today.findChildren()[6].text]
    return prayerTimes[whichTime]

###

### PROGRAM

while True:
    option = input("\nWelcome to AdhanTime. To navigate the menus, type PRAYER to display prayer times, ABOUT for program information, or EXIT to exit the program.\n")

    if option == "PRAYER":
        print("\nToday is " + date)
        time = input("Which prayer time would you like to know about? Type in FAJR, DHUHR, ASR, MAGHRIB, or ISHA.\n")

        if time == "FAJR":
            output = prayer(0)
            print("FAJR: " + output)

        elif time == "DHUHR":
            output = prayer(1)
            print("DHUHR: " + output)

        elif time == "ASR":
            output = prayer(2)
            print("ASR: " + output)

        elif time == "MAGHRIB":
            output = prayer(3)
            print("MAGHRIB: " + output)

        elif time == "ISHA":
            output = prayer(4)
            print("ISHA: " + output)

        print("Exiting back to main menu ...")

    elif option == "ABOUT":
        print("Created by Labib Mahmud.\nhttps://labibm.netlify.app")

    elif option == "EXIT":
        print("Exiting program ...")
        sys.exit()

    else:
        print("No input detected. Exiting ...")
        sys.exit()

###
