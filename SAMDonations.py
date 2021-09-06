#! python3
# SAMDonations.py - Retrieves donations from streamlabs, uses SAM to read out
# the donator name and donation amount, then splits up the donation message
# into 100 chr strings to bypass SAM chr limit and uses it to read them out 
# sequentially.
# Note: For this code to work as-is, you need to have Sebastian Macke's port 
# of the SAM software on your PC and set in the Path system environment
# variable.

import os
import time
import math
import requests

def mainLoop:
    donation = None
    # TODO: Create infinite loop with 3s pause at end
    while True
    time.sleep(13)
        #TODO: Retrieve donations, compare to existing donation variable. If new donations, return them. Else, 
# TODO: 
# TODO: 
# TODO: 
# TODO: 
# TODO: 

test = """This is a test string. But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"""

totalLength = len(test)

start = 0

# calculate amount of <=100 chr strings needed and iterate that many times.
for i in range(math.ceil(totalLength / 100)):
# check whether slice upper bound would be too high, and use final index instead
    if start + 100 <= totalLength:
        os.system(f"cmd /c sam {test[start:start+100]}")
    else:
        os.system(f"cmd /c sam {test[start:totalLength-1]}")
    start += 100