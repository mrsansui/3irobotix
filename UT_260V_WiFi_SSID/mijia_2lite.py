# -*- coding: utf-8 -*-
import time
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common_para import *


# 米家模组
class MiHome_M6:
    def __init__(self, platformname, platformversion, devicename):
        print("## 欢迎使用米家自动化模组 ## ")
        caps = {"platformName": platformname,
                "platformVersion": platformversion,
                "deviceName": devicename,
                "appPackage": "com.xiaomi.smarthome",
                "appActivity": ".SmartHomeMainActivity",
                "newCommandTimeout": 10000,  # Appium在没有收到下一个命令时，默认超时时间是60s，超时后应用将会自动关闭
                "noReset": "True"}  # 不重置qpp数据:True   重置qpp数据:False
        #       "autoAcceptAlerts": true ,默认选择接受弹窗的条款
        print("--->开始连接%s" % devicename)
        try:
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)  # 启动app

        except:
            self.driver.close()
            print("连接设备超时，请确保appium服务器已开启，已连接设备并打开USB调试后再开始运行")

        else:
            print("--->启动米家app")

    # 添加设备
    def add_device(self):
        print("--->添加设备")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="添加设备"]').click()
        driver.find_element_by_id('com.xiaomi.smarthome:id/add_device_tv').click()  # 添加设备
        driver.find_element_by_id('com.xiaomi.smarthome:id/mj_search_btn').click()  # 搜索按钮
        driver.find_element_by_class_name('android.widget.EditText').send_keys("小米扫拖机器人2 Lite")
        driver.find_element_by_xpath('//android.widget.TextView[@text="小米扫拖机器人2 Lite"]').click()
        driver.find_element_by_id('com.xiaomi.smarthome:id/tips').click()  # 确认上述操作：同时按下了Home+回充
        driver.find_element_by_id('com.xiaomi.smarthome:id/next_btn').click()
        driver.find_element_by_xpath('//android.widget.TextView[@text="连接其他路由器"]').click()
        router_xpath = '//android.widget.TextView[@text="{}"]'.format(new_ssid)
        driver.find_element_by_xpath(router_xpath).click()
        # 输入密码
        try:
            driver.find_element_by_id('com.xiaomi.smarthome:id/password_input_et').send_keys(new_pwd)
            driver.find_element_by_id('com.xiaomi.smarthome:id/right_button').click()  # 确定
        except:
            pass
        driver.find_element_by_id('com.xiaomi.smarthome:id/next_btn').click()  # 下一步
        print("-->Connecting to the network, please wait")

        driver.find_element_by_xpath('//android.widget.TextView[@text="Rel-test"]').click()
        driver.find_element_by_id('com.xiaomi.smarthome:id/sb_common_set').click()  # 设为首页常用设备-关闭
        driver.find_element_by_id('com.xiaomi.smarthome:id/skip').click()  # 下一步
        driver.find_element_by_id('com.xiaomi.smarthome:id/go_next').click()  # 下一步
        driver.find_element_by_id('com.xiaomi.smarthome:id/go_next').click()  # 开始体验
        sleep(2)
        driver.find_element_by_id('com.xiaomi.smarthome:id/agree').click()
        print("Successfully connected to WiFi")

    # 向左滑动。y轴保持不变，X轴：由大变小
    def swipe_left(self, star_x=0.9, stop_x=0.1, duration=2000):
        driver = self.driver
        x = driver.get_window_size()["width"]
        y = driver.get_window_size()["height"]
        x1 = int(x * star_x)
        y1 = int(y * 0.5)
        x2 = int(x * stop_x)
        y2 = int(y * 0.5)
        driver.swipe(x1, y1, x2, y2, duration)
        # driver.tap([(700, 1800)], 5)
        # driver.find_element_by_xpath('//android.widget.Button[@content-desc="返回"]').click()

    # 向下滑动。x轴保持不变，y轴：由小变大
    def swipe_down(self, start_y=0.1, stop_y=0.9, duration=1000):
        driver = self.driver
        x = driver.get_window_size()["width"]
        y = driver.get_window_size()["height"]
        x1 = int(x * 0.5)
        y1 = int(y * start_y)
        x2 = int(x * 0.5)
        y2 = int(y * stop_y)
        driver.swipe(x1, y1, x2, y2, duration)

    # 进入设备（房间名，设备名）
    def enter_the_device(self, room_name, devices_name):
        '''

        :param self:
        :param room_name: Rel-test
        :param devices_name: 扫地机器人2 Lite
        :return:
        '''
        driver = self.driver
        driver.implicitly_wait(30)

        try:
            driver.find_element_by_android_uiautomator("text(\"%s\")" % room_name).click()
            print("--->进入%s中设备的控制界面" % room_name)
        except:
            pass

    # 删除设备（房间名）
    def delete_device(self):
        print("--->开始删除设备")
        driver = self.driver
        driver.implicitly_wait(30)
        try:
            antion_1 = TouchAction(driver)
            element1 = driver.find_element_by_id(r'com.xiaomi.smarthome:id/ddx')
            antion_1.long_press(element=element1, duration=4000).wait(5000).perform()
        except:
            pass

        driver.find_element_by_android_uiautomator("text(\"删除设备\")").click()
        driver.find_element_by_id('com.xiaomi.smarthome:id/button1').click()
        time.sleep(3)
        print("--->删除设备成功")


if __name__ == '__main__':
    MiHome_260v = MiHome_M6('Android', '10.0', 'HUAWEI-M6')
    MiHome_260v.add_device()
    MiHome_260v.swipe_left()
    MiHome_260v.swipe_down()
    MiHome_260v.enter_the_device('Rel-test', r'扫地机器人2 Lite')
    MiHome_260v.delete_device()
