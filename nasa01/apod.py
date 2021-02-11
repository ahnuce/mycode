#!/usr/bin/env python3
#import requests

## Define APOD 
#apodurl = 'https://api.nasa.gov/planetary/apod?'
#mykey = 'api_key=DEMO_KEY'    ## your key goes in place of DEMO_KEY

## Call the webservice
#apodurlobj = requests.get(apodurl + mykey)

## read the file-like object
#apodread = apodurlobj.json()

## display our Pythonic data
#print("\n\nConverted Python data")
#print(apodread)

#!/usr/bin/env python3
import requests
from pprint import pprint as pp # part of the standard libray
# import webbrowser

## define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our API to call
MYKEY = 'api_key=u5xr4guqlhijBJaVhzM2p7dAK2ylVGvTTc4l9C9v' ## this is our api key

## pretty print json
def main():
    """run-time code"""
    nasaapiobj = requests.get(NASAAPI + MYKEY) # call the webservice
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    # Show converted json
    print(nasaread) # show converted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # Show Pretty Print json
    pp(nasaread) # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(nasaread['explanation']) # display the value for the key explanation
    print("Link to the APOD:", nasaread.get('hdurl',"No HD URL for today!"))

    #allow user to optionally input the date of the image they'd like to view
    inputdate= input('\nDate of image you would like to view (YYYY-MM-DD)')
    nasaapiobj = requests.get(NASAAPI + MYKEY + "&date=" + inputdate)
    print(nasaapiobj).json()
    print("this is what im testin")

    #input('\nPress ENTER to view this photo of the day') # pause for ENTER
    # webbrowser.open(nasaread['hdurl']) # open in the webbrowser

main()

