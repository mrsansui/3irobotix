# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, sys, os

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome()
driver.implicitly_wait(10)
Tenda_F3 = "http://192.168.0.1/"
XiaoMi_3_Pro = "http://192.168.31.1/"
HUAWEI_Hi = "http://192.168.3.1/"
def print_current_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return current_time
def router_xiaomi():
    driver.get(XiaoMi_3_Pro)
    driver.maximize_window()
    time.sleep(2)
    login = driver.find_element_by_id("password")
    login.click()
    login.send_keys("123456789")
    driver.find_element_by_id("btnRtSubmit").click()
    time.sleep(2)
    # 跳转到常用设置
    driver.find_element_by_xpath('//*[@id="nav"]/ul/li[3]/a').click()
    time.sleep(2)

    ssid_box = driver.find_element_by_xpath('//*[@id="wifiset24"]/div[2]/span/input')
    current_ssid = ssid_box.get_attribute("value")
    print('current_ssid: ',current_ssid)
    # 清空WiFi输入框
    ssid_box.clear()

    # 需要修改的WiFi名称
    new_ssid = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDE'
    print('new_ssid: ', new_ssid)
    ssid_box.send_keys(new_ssid)
    # 回车保存
    ssid_box.send_keys(Keys.ENTER)
    time.sleep(2)
    # 点击确认
    confirm_btn = driver.find_element_by_xpath('//div[1]/div/div[3]/div/a[1]')
    confirm_btn.click()
    time.sleep(2)
    driver.refresh()
    return new_ssid

def router_tenda():
    driver.get(Tenda_F3)
    # driver.maximize_window()
    time.sleep(2)
    print("1******")
    wireless_cfg = driver.find_element_by_xpath('//*[@id="wireless"]')
    print("2******")
    wireless_cfg.click()
    time.sleep(2)
    ssid_box = driver.find_element_by_xpath('//*[@id="wifiSSID"]')
    # current_ssid = ssid_box.get_attribute("value")
    # print('current_ssid: ', current_ssid)
    # 清空WiFi输入框
    ssid_box.clear()
    # 需要修改的WiFi名称
    new_ssid = 'test_tenda'
    print('new_ssid: ', new_ssid)
    ssid_box.send_keys(new_ssid)
    time.sleep(1)
    # 点击确认
    confirm_btn = driver.find_element_by_xpath('//*[@id="submit"]')
    confirm_btn.click()
    # 弹窗确认
    alert = driver.switch_to.alert
    alert.accept()
    print("%s is setting..." % new_ssid)
    driver.quit()
    return new_ssid

def reconnect_wifi(new_ssid):

    os.system("netsh wlan add profile filename=WLAN-%s.xml" % new_ssid)
    time.sleep(2)
    os.system("netsh wlan connect name=%s" % new_ssid)
    print("reconnecting wifi with %s, please wait" % new_ssid)

if __name__ == '__main__':
    new_ssid = 'test_tenda'
    print_current_time()
    router_tenda()
    reconnect_wifi(new_ssid)
