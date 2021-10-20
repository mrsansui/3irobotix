# _*_ coding:utf-8 _*_
from selenium import webdriver
import time, sys, os
driver = webdriver.Chrome()
# router ip addr XiaoMi
router_ip = "192.168.3.1"

def print_current_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return current_time
driver.get("http://192.168.31.1/")
time.sleep(3)
login = driver.find_element_by_id("password")
login.click()
login.send_keys("1234567890")
driver.find_element_by_id("loginbtn").click()
time.sleep(2)
driver.find_element_by_class_name("want_wifi").click()
time.sleep(2)
value = driver.find_element_by_id("content_wifi_name2G_ctrl").get_attribute("value")
print(value)

# SSID = driver.find_element_by_id("content_wifi_name2G_ctrl")
# SSID.click()
# SSID.clear()
# time.sleep(1)
# SSID.send_keys("hzx2")
# time.sleep(2)
# driver.find_element_by_id("SsidSettings_submitbutton").click()
# driver.refresh()

time.sleep(3)
print("！！！")
