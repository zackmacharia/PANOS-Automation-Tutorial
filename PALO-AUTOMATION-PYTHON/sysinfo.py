# from urllib import request
# import ssl
# import api_key

import os
import requests
import urllib3

# This command suppresses SSL error message displaying on the console
urllib3.disable_warnings()

DEVICE = os.getenv("PANORAMA")
APIKEY = os.getenv("PANOAPIKEY")

def get_sys_info(DEVICE):
    """Request System Info from Palo Alto Netowrks Firewall or Panorama"""
    url = 'https://' + DEVICE + \
        '/api/?type=op&cmd=<show><system><info></info></system></show>&key=' +\
              APIKEY

    # keyResponse: stores the response code from the device this is of type Response e.g. 403, 200
    fw_response = requests.get(url, verify=False)

    # keyText: converts Response type to a string
    fw_response_text = fw_response.text
    
    print(fw_response)

if __name__ == "__main__":
    get_sys_info(DEVICE)