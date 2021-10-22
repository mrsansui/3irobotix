import os
import time
import xml
import xml.dom.minidom
import xml.etree.ElementTree as ET
from common_para import *

ET.register_namespace("","http://www.microsoft.com/networking/WLAN/profile/v1")

def xml_wlan_cfg():
    # this function only can used in changeing password
    print("current work directory: ",os.getcwd())
    os.chdir("C:\\Users\\Administrator")
    print("change work directory to: ", os.getcwd())
    file_xml = 'C:\\Users\\Administrator\\WLAN-tenda_3i.xml'
    # tree = ET.parse(file_xml)
    # root = tree.getroot()
    # name = root.find('name')
    dom = xml.dom.minidom.parse(file_xml)
    root = dom.documentElement
    names = root.getElementsByTagName('name')
    current_wifi_name = names[0].firstChild.data
    names[0].firstChild.data = new_ssid
    names[1].firstChild.data = new_ssid
    print(current_wifi_name, "--->", new_ssid)
    print('reconnect to %s ' % new_ssid)
    # save wlan cfg xml file
    with open("C:\\Users\\Administrator\\WLAN-%s.xml" % new_ssid, 'w') as f:
        dom.writexml(f)
        print("The WiFi name has been changed successfully, please reconnect to %s" % new_ssid)

def reconnect_wifi():
    # netsh wlan show profiles
    # os.system("netsh wlan add profile filename=WLAN-%s.xml" % new_ssid)
    time.sleep(2)
    os.system("netsh wlan connect name=%s" % new_ssid)
    time.sleep(5)
    print("Connecting to %s, please wait, or try to connect to the wireless network manually" % new_ssid)

# reconnect_wifi()