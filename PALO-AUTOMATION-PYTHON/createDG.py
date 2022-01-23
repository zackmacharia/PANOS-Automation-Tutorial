import os
from panos import panorama

DEVICE = os.getenv("PANORAMA")
APIKEY = os.getenv("PANOAPIKEY")

pano = panorama.Panorama(hostname=DEVICE, api_key=APIKEY)

# dg: value of the device group name you want to create in Panorama
dg = "Test6"

# createDG creates a dg object then adds the dg to the object and finally creates it to the device
def createDG(name):
    dg = panorama.DeviceGroup(name)
    pano.add(dg) 
    dg.create() 
    print(name, "device group successfully created!")


if __name__ == "__main__":
    createDG(dg)

    