import re
import os
import requests
import urllib3

# This command suppresses SSL error message displaying on the console
urllib3.disable_warnings()

# These constants represent environmental variables created in the user's system e.g. laptop
USERNAME = os.getenv("PANOUSER")
PASSWORD = os.getenv("PANOPWD")
DEVICE = os.getenv("PANORAMA")

def generateapikey(DEVICE, USERNAME, PASSWORD):
    # url: specifies the URL format required to get the API key from the device
    url = "https://" + DEVICE + "/api/?type=keygen&" + "user=" + USERNAME + "&password=" + PASSWORD 

    # keyResponse: stores the response code from the device this is of type Response e.g. 403, 200
    keyResponse = requests.get(url, verify=False)
    print("Key Response:", keyResponse)

    # keyText: converts Response type to a string
    keyText = keyResponse.text
    print("Key Text:", keyText)

    grepApiKey(keyText, "key")
    

def grepApiKey(responseText, value):
    
    # pattern: regular expression pattern used to filter out the required value
    # The function takes a string of the text to be parsed

    pattern = re.compile(r"<key>(.*?)</key>")
    search = re.search(pattern, responseText)
    key = search.group(1) # targeting group with API key information
    print("")
    print("API KEY:",key,"\n")


if __name__ == "__main__":
    generateapikey(DEVICE, USERNAME, PASSWORD)
