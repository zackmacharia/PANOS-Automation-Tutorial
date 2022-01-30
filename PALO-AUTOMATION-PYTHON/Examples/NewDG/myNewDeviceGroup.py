import os # This package allows the script to interact with the computer operating system
from panos import panorama # This is the panorama module from pan-os-python library

"""
For security reasons instead of hardcoding the API Key (credentials) on the script. It's better to use environmental variables.
Below are the steps I used to create envrionmental variables in MACOS
Open Terminal

`nano ~/.bash_profile`
export PANORAMA="PANORAMAFQDN_OR_IPADDRESS"
export PANOAPIKEY="APIKEYVALUEHERE"
:q!
ctrl+0
ctrl+X

Restart the session either by closing out the terminal or running the source command. 
"source ~/.bash_profile"
Press Enter

Verify the environmental variables by running:

"printenv | grep PANO"
"""
DEVICE = os.getenv("PANORAMA")
APIKEY = os.getenv("PANOAPIKEY")

pano = panorama.Panorama(hostname=DEVICE, api_key=APIKEY)

# createDG creates a dg object then adds the dg to the object and finally creates it to the device
def createDG(name):
    dg = panorama.DeviceGroup(name) # this line creates DeviceGroup PanObject
    pano.add(dg) # adds the devicegroup into the PanObject
    dg.create()  # creates the devicegroup in the live Panorama device
    print(name, "device group successfully created!")


if __name__ == "__main__":
    createDG("MyNewDeviceGroup")

    