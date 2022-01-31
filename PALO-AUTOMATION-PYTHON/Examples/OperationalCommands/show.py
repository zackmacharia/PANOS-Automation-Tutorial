"""
The os library is used to interact with the computer operating system
The panorama module from the panorama library is used to interact with Panorama
"""

import os 
from panos import panorama 

"""
For security reasons instead of hardcoding the API Key (credentials) on the script. It's better to use environmental variables.
Below are the steps I used to create envrionmental variables in MACOS
Open Terminal

`nano ~/.bash_profile`
`export PANORAMA="PANORAMAFQDN_OR_IPADDRESS"`
`export PANOAPIKEY="APIKEYVALUEHERE"`
`:q!`
`ctrl+0`
`ctrl+X`

Restart the session either by closing out the terminal or running the source command. 
`"source ~/.bash_profile"`
`Press Enter`

Verify the environmental variables by running the command below on the Terminal:

`"printenv | grep PANO"`
"""

# Assigns the environmental values to a constant
DEVICE = os.getenv("PANORAMA") 
APIKEY = os.getenv("PANOAPIKEY") 

# Instantiate Panorama PanObject and connect to live device
pano = panorama.Panorama(hostname=DEVICE, api_key=APIKEY)

def show_clock():
    "This command returns an ElementTree output"
    print(pano.op('show clock'))

def show_clock_xml():
    "This command returns a Bytes output"
    print(pano.op('show clock', xml=True))


if __name__ == "__main__":
    show_clock()
    show_clock_xml()