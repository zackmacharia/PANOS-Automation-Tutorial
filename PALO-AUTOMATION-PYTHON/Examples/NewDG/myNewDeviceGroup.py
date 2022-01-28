import os
from panos import panorama

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

    