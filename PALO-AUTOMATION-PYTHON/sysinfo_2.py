import os
from panos import panorama

DEVICE = os.getenv("PANORAMA")
APIKEY = os.getenv("PANOAPIKEY")

pano = panorama.Panorama(hostname=DEVICE, api_key=APIKEY)

def sysinfo(pano):
    """Request System Info from Palo Alto Netowrks Firewall or Panorama"""

    # sysinfo_resp: stores the response code from the device this is of type Response e.g. 403, 200
    sysinfo_resp = pano.op('show system info')  

    # xml_sysinfo_resp: displays info in human readable format
    xml_sysinfo_resp = pano.op('show system info', xml=True)
    print(xml_sysinfo_resp)

if __name__ == "__main__":
    sysinfo(pano)
