from pywifi import const, PyWiFi, Profile
import time
from common_para import *

def is_wifi_connect(wifi_name, wifi_password):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()  # 断开网卡连接 time.sleep(3)# 缓冲3秒
    profile_info = Profile()         # wifi配置文件
    profile_info.ssid = wifi_name    # wifi名称
    profile_info.auth = const.AUTH_ALG_OPEN         # 需要密码
    profile_info.akm.append(const.AKM_TYPE_WPA2PSK)    # 加密类型
    profile_info.cipher=const.CIPHER_TYPE_CCMP # 加密单元
    profile_info.key = wifi_password        # wifi密码
    iface.remove_all_network_profiles()     # 删除其他配置文件
    # tmp_profile = iface.add_network_profile(profile_info)       # 加载配置文件
    tempfile = iface.add_network_profile(profile_info)
    iface.connect(tempfile)      # 连接
    time.sleep(5)                   # 尝试5秒能否成功连接
    if iface.status() == const.IFACE_CONNECTED:
        print("%s: connected successfully!" % wifi_name)
    else:
        print("%s: connected failed!" % wifi_name)

if __name__ == '__main__':
    is_wifi_connect(new_ssid, new_pwd)