#! python3
"""SAMDonations.py - Retrieves donations from streamlabs, uses SAM to
read out the donator name and donation amount, then splits up the
donation message into individual word strings to bypass SAM chr limit
and uses it to read them out sequentially.

Note: For this code to work as-is, you need to have Sebastian Macke's
port of the SAM software on your PC and either set in the Path system
environment variable or in the same folder as this script."""

# Why no, I'm not a good programmer. How did you guess?

import os
import time
import requests
import json

# Just so SAM reads it properly.
CURRENCIES = {"AUD": "Australian Dollars", "BRL": "Brazilian Reais",
              "CAD": "Canadian Dollars", "CZK": "Czech Korunas",
              "DKK": "Danish Kroner", "EUR": "Euros",
              "HKD": "Hong Kong Dollars", "ILS": "Israeli New Sheqels",
              "MYR": "Malaysian Ringgit", "MXN": "Mexican Pesos",
              "NOK": "Norwegian Kroner", "NZD": "New Zealand Dollar",
              "PHP": "Philippine Pesos", "PLN": "Polish Zloty",
              "GBP": "Pound Sterling", "RUB": "Russian Rubles",
              "SGD": "Singapore Dollars", "SEK": "Swedish Kronur",
              "CHF": "Swiss Francs", "THB": "Thai Baht",
              "TRY": "Turkish Liras", "USD": "U.S. Dollars"}
# Change this to the path of your access token file.
# You shouldn't really use a plaintext file, but I'm lazy.
# Would be better to instead store it somewhere secure and have input()
# prompt you for it
TOKEN_FILE = open("accessToken.txt")
ACCESS_TOKEN = TOKEN_FILE.read()
TOKEN_FILE.close()
URL = "https://streamlabs.com/api/v1.0/donations"
HEADERS = {"Accept": "application/json"}


def mainLoop():
    print("Getting most recent donation ID...")
    try:
        # Gets donations in json, converts it to a python dict, then gets the
        # ID of the most recent donation and converts it to int. It's all we
        # need.
        ID = int(json.loads(requests.request("GET", URL, headers=HEADERS,
                            params={"access_token": ACCESS_TOKEN}
                                    ).text)["data"][0]["donation_id"])
        print("Got it.\nScanning (13 second delay)...")
    except IndexError:
        ID = "1"
        print("No donations found.")
    # delay due to testing status, bug me to fix it if this becomes public
    time.sleep(13)
    while True:
        # resets start number, then retrieves new donations
        newDonations = json.loads(requests.request(
                                  "GET", URL, headers=HEADERS,
                                  params={"access_token": ACCESS_TOKEN,
                                          "after": ID}).text)["data"]
        # if there are any new donations, reads the oldest and sets the
        # new start ID
        if newDonations:
            currentDonation = newDonations[-1]
            ID = currentDonation["donation_id"]

            # Reads out the name, amount, and currency of the donation.
            # Split up to avoid character limit.
            os.system(f"cmd /c sam {currentDonation['name']} donated ")
            os.system(f"cmd /c sam {str(float(currentDonation['amount']))}")
            os.system(f"cmd /c sam {CURRENCIES[currentDonation['currency']]}")
            # slight pause before reading the message
            time.sleep(0.5)

            message = currentDonation["message"]
            if message:
                mesWords = message.split(" ")
                for word in mesWords:
                    os.system("sam -pitch 75 -throat 100 -mouth 150"
                              f"{word}")
            time.sleep(13)
        else:
            time.sleep(13)
            continue


mainLoop()
