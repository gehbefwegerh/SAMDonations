# SAMDonations
 Reads Streamlabs donations using a SAM port
 
 
Look, it's kinda janky. You need to paste your access token into accessToken.txt for it to work.


In addition, you need to download Sebastian Macke's SAM port for Windows, and add the file to your PATH. Instructions on how to add a file to your PATH can be found via google. 
The port can be found here: https://simulationcorner.net/index.php?page=sam


If you want to use the SAMTest.bat, which is just to test that the program is working properly, you also need to add your access token to that file. Instructions can be found inside the file.

Detailed instructions (since I had to write them out anyway):
You have 2 options:

For both methods:
1. Download the files from the github repository and put them in a folder together.
2. Download SAM (link in readme.md), and add it to your system PATH.
3. Open accessToken.txt in a text editor, enter your API access token, and save the file.
4. (Optional) Open SAMTest.bat in a text editor, and add your access token to SAMTest.bat where instructed in the file. Run the file while SAMDonations is running to test that the main program is working correctly.

Option 1: Using the exe (easier, but of course more suspicious)
1. Run SAMDonations.exe, and wait for donations.

Option 2: Using the SAMDonations.py file. (harder, but you can check the code, therefore safer)
1. Install python, making sure to add it to your PATH
2. Open command prompt at the SAMDonations.py folder.
3. type "pip install -r requirements.txt" into the command prompt to install all dependencies for this software.
4. Run SAMDonations.py
