#! python3
"""SAMDonations.py - Retrieves donations from streamlabs, uses SAM to
read out the donator name and donation amount, then splits up the
donation message into 100 chr strings to bypass SAM chr limit and uses
it to read them out sequentially.
Note: For this code to work as-is, you need to have Sebastian Macke's
port of the SAM software on your PC and either set in the Path system
environment variable or in the same folder as this script."""

# Why no, I'm not a good programmer. How did you guess?

import os
import time
import math
import requests
import json

CURRENCIES = {"AUD":"Australian Dollars", "BRL":"Brazilian Reais",
              "CAD":"Canadian Dollars", "CZK":"Czech Korunas", 
              "DKK":"Danish Kroner", "EUR":"Euros", "HKD":"Hong Kong Dollars",
              "ILS":"Israeli New Sheqels", "MYR":"Malaysian Ringgit",
              "MXN":"Mexican Pesos", "NOK":"Norwegian Kroner",
              "NZD":"New Zealand Dollar", "PHP":"Philippine Pesos",
              "PLN":"Polish Zloty", "GBP":"Pound Sterling",
              "RUB":"Russian Rubles", "SGD":"Singapore Dollars",
              "SEK":"Swedish Kronur", "CHF":"Swiss Francs", "THB":"Thai Baht",
              "TRY":"Turkish Liras", "USD":"U.S. Dollars"}
# Change this to the path of your access token file.
# You shouldn't really use a plaintext file, but I'm lazy. 
# Would be better to instead store it somewhere secure and have input()
# prompt you for it
TOKEN_FILE = open("accessToken.txt")
ACCESS_TOKEN = TOKEN_FILE.read()
TOKEN_FILE.close()
URL = "https://streamlabs.com/api/v1.0/donations"
HEADERS = {"Accept": "application/json"}
# Gets donations in json, converts it to a python dict, then gets the 
# ID of the most recent donation and converts it to int. It's all we 
# need.
START_DONATION_ID = int(json.loads(requests.request("GET", URL, headers=HEADERS,
                  params={"access_token":ACCESS_TOKEN}).text
                  )["data"][0]["donation_id"])
# delay due to testing status, bug me to fix it if this becomes public
time.sleep(13)

def mainLoop(ID):
    while True:
        start = 0
        newDonations = json.loads(requests.request("GET", URL, headers=HEADERS,
                                  params={"access_token":ACCESS_TOKEN,
                                          "after":ID}).text)["data"]
        if newDonations:
            currentDonation = newDonations[-1]
            ID = currentDonation["donation_id"]
            
            os.system(f"cmd /c sam {currentDonation['name']} donated " + 
                       f"{str(float(currentDonation['amount']))} " +
                       f"{CURRENCIES[currentDonation['currency']]}")
            time.sleep(1)
            
            message = currentDonation["message"]
            if message:
                messageLen = len(message) # real creative
                # calculate amount of <=100 chr strings needed and
                # iterate that many times.
                for i in range(math.ceil(messageLen / 100)):
                    # takes a 100 chr slice, says it, then adds 100 to start there next time.
                    if start + 100 <= messageLen:
                        os.system(f"cmd /c sam --pitch 80 {message[start:start+100]}")
                        start += 100
                    # check whether slice upper bound would be too high, and use final index instead
                    else:
                        os.system(f"cmd /c sam --pitch 80 {message[start:messageLen-1]}")

            time.sleep(13)
        else:
            time.sleep(13)
            continue


# mainLoop(START_DONATION_ID)
mainLoop(156694052)