# author: chenzq2301@3irobotics.com
# created: 2021/09/08

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

def open_mijia():
    desired_caps = {"platformName": 'Android',
                    "platformVersion": '10.0',
                    "deviceName": 'HUAWEI-M6',
                    "appPackage": "com.xiaomi.smarthome",
                    "appActivity": ".SmartHomeMainActivity",
                    "newCommandTimeout": 10000,  # Appium在没有收到下一个命令时，默认超时时间是60s，超时后应用将会自动关闭
                    "noReset": "True"}  # 不重置qpp数据:True   重置qpp数据:False
                    # "autoAcceptAlerts": true ,默认选择接受弹窗的条款
    '''
    
    # desired_caps=dict()
    # desired_caps['platformName']='Android'
    # desired_caps['platformVersion']='10.0'
    # desired_caps['deviceName']='RCJ6R20806001474'
    # 
    # desired_caps['noReset'] = True
    # desired_caps['fullReset'] = False
    # desired_caps['appPackage']='com.xiaomi.smarthome'
    # desired_caps['appActivity']='.SmartHomeMainActivity'
    '''

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # input("Please enter any character to terminate:")
    return driver
# def add_device():


def long_press(driver):
    antion_1 = TouchAction(driver)
    element1 = driver.find_element_by_id(r'com.xiaomi.smarthome:id/ddx')
    antion_1.long_press(element=element1,duration=4000).wait(5000).perform()

# driver.quit()
    loc = ()


driver = open_mijia()
