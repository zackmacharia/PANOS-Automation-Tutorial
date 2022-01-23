import os
from panos import panorama

USERNAME = os.getenv("PANOUSER")
PASSWORD = os.getenv("PANOPWD")
DEVICE = os.getenv("PANORAMA")

pano = panorama.Panorama(DEVICE, USERNAME, PASSWORD)

def sysinfo(pano):
    """Request System Info from Palo Alto Netowrks Firewall or Panorama"""

    # sysinfo_resp: stores the response code from the device this is of type Response e.g. 403, 200
    sysinfo_resp = pano.op('show system info')  

    # xml_sysinfo_resp: displays info in human readable format
    xml_sysinfo_resp = pano.op('show system info', xml=True)
    print(xml_sysinfo_resp)

if __name__ == "__main__":
    sysinfo(pano)
