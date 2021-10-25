# author: chenzq2301@3irobotics.com
# created: 2021/09/08
# 适用场景:
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

def open_mijia():

    desired_caps=dict()
    desired_caps['platformName']='Android'
    desired_caps['platformVersion']='10.0'
    desired_caps['deviceName']='HUAWEI M6'
    desired_caps['noReset'] = True
    desired_caps['fullReset'] = False
    desired_caps['appPackage']='com.xiaomi.smarthome'
    desired_caps['appActivity']='.SmartHomeMainActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver

def long_press(driver):
    antion_1 = TouchAction(driver)
    element1 = driver.find_element_by_id(r'com.xiaomi.smarthome:id/ddx')
    antion_1.long_press(element=element1,duration=4000).wait(5000).perform()

# driver.quit()

