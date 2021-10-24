# -*- coding: utf-8 -*-
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 米家模组
class MiHomeModule:
    def __init__(self, platformname, platformversion, devicename):
        print("***###[欢迎使用米家自动化模组]###***")
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

    # 米家登录
    def mihome_login(self):
        print("--->自动登录中")
        driver = self.driver
        time.sleep(1)  # app启动后等待1秒，方便元素加载完成
        driver.implicitly_wait(30)
        try:
            # driver.find_element_by_id('com.xiaomi.smarthome:id/textView1').click()
            locator = (By.ID, "com.xiaomi.smarthome:id/textView1")  # 通过id查找
            # 显示等待30秒，没0.5查找一次ID，将通过ID查找到的元素进行文本匹配，until做一个判断
            WebDriverWait(driver, 2, 0.5).until(EC.text_to_be_present_in_element(locator, "立即登录"))
            # driver.find_element_by_id('com.xiaomi.smarthome:id/textView1').click()

        except:
            driver.find_element_by_id("com.xiaomi.smarthome:id/ok").click()  # 同意并继续（声明与条款）
            time.sleep(1)
            driver.find_element_by_id("com.xiaomi.smarthome:id/ok").click()  # 同意（体验者计划）
            driver.find_element_by_id("com.xiaomi.smarthome:id/btn_confirm").click()  # 立即体验
            # driver.find_element_by_id("com.xiaomi.smarthome:id/select_all_check_box").click()  # 全选
            # driver.find_element_by_id("com.xiaomi.smarthome:id/next_btn").click()  # 下一步
            # driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()  # 定位权限

        finally:
            driver.find_element_by_id("com.xiaomi.smarthome:id/textView1").click()  # 立即登录
            driver.find_element_by_id("com.xiaomi.smarthome:id/userId").send_keys("18390942002")  # 输入登录账号和密码，点击登录
            driver.find_element_by_id("com.xiaomi.smarthome:id/password").send_keys("2017woaini")
            driver.find_element_by_id("com.xiaomi.smarthome:id/sign_in_btn").click()

            time.sleep(5)
            print("--->登录成功")

    # 米家配网
    def mihome_distribution_network(self, devices_name, wifi_name):
        driver = self.driver
        # 隐式等待
        driver.implicitly_wait(30)
        # 展开按钮
        print("--->开始配网")
        locator_navigation = (By.ID, "com.xiaomi.smarthome:id/arrow_down_img")
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located(locator_navigation))
        TouchAction(driver).tap(x=957, y=137).perform()
        el1 = driver.find_element_by_id("com.xiaomi.smarthome:id/search_et")  # 点击搜索框
        el1.click()
        el1.send_keys(devices_name)  # 输入要查找的设备种类
        driver.find_element_by_id("com.xiaomi.smarthome:id/scan_desc").click()  # 点击查找到的第一个设备类型
        driver.find_element_by_id("com.xiaomi.smarthome:id/check_box_confirm").click()  # 操作指引界面，勾选
        driver.find_element_by_id("com.xiaomi.smarthome:id/next_btn").click()  # 下一步

        locator_title = (By.ID, "com.xiaomi.smarthome:id/module_a_3_return_title")  # 通过id查找
        try:
            # 显示等待60秒，没0.5查找一次ID，将通过ID查找到的元素进行文本匹配，until做一个判断
            WebDriverWait(driver, 42).until(EC.text_to_be_present_in_element(locator_title, "选择路由器"))
        except:
            # 一直扫描不到？尝试手动连接 id：com.xiaomi.smarthome:id/connect_failed_tips
            # 继续扫描 id:com.xiaomi.smarthome:id/button1
            print("未找到设备,请确认设备已重置wifi，重新尝试扫描")
            driver.find_element_by_id("com.xiaomi.smarthome:id/button1").click()
            WebDriverWait(driver, 40).until(EC.text_to_be_present_in_element(locator_title, "选择路由器"))

        print("开始连接网络'%s'" % wifi_name)
        # 通过文本定位需要使用uiautomator的定位方式，使用text的内容：driver.find_element_by_android_uiautomator("text（\文本\）")
        driver.find_element_by_android_uiautomator("text(\"%s\")" % wifi_name).click()  # 荣耀_2.4G
        driver.find_element_by_id("com.xiaomi.smarthome:id/next_btn").click()
        # 完成 id：com.xiaomi.smarthome:id/common_btn
        # 添加设备成功 id：com.xiaomi.smarthome:id/progress_title
        locator_finish = (By.ID, "com.xiaomi.smarthome:id/common_btn")
        WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element(locator_finish, "完成"))
        driver.find_element_by_id("com.xiaomi.smarthome:id/common_btn").click()

        # 判断有无房间名
        try:
            driver.find_element_by_android_uiautomator("text(\"米家S1配网自动化\")").click()

        except Exception:
            print('正在创建房间"米家S1配网自动化"')
            driver.find_element_by_accessibility_id("添加").click()
            driver.find_element_by_id('com.xiaomi.smarthome:id/client_remark_input_view_edit').send_keys("米家S1配网自动化")
            driver.find_element_by_id('com.xiaomi.smarthome:id/button1').click()

        driver.find_element_by_id('com.xiaomi.smarthome:id/skip').click()  # 下一步
        device_name = driver.find_element_by_id('com.xiaomi.smarthome:id/device_name')
        device_name.clear()
        device_name.send_keys(devices_name)  # 更改设备名
        driver.find_element_by_id('com.xiaomi.smarthome:id/go_next').click()  # 下一步
        driver.find_element_by_android_uiautomator("text(\"开始体验\")").click()

        try:
            print("正在跳过清扫指引")
            # 同意并继续 id：com.xiaomi.smarthome:id/agree
            locator_finish = (By.ID, "com.xiaomi.smarthome:id/agree")
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(locator_finish, "同意并继续"))
            driver.find_element_by_android_uiautomator("text(\"同意并继续\")").click()
            screensize = driver.get_window_size()
            x1 = screensize['width'] * 0.9
            y1 = screensize['height'] * 0.5
            x2 = screensize['width'] * 0.1
            driver.swipe(x1, y1, x2, y1)
            time.sleep(0.2)
            driver.swipe(x1, y1, x2, y1)
            time.sleep(0.2)
            driver.swipe(x1, y1, x2, y1)
            time.sleep(0.2)
            driver.swipe(x1, y1, x2, y1)
            time.sleep(0.5)
            driver.find_element_by_android_uiautomator("text(\"去设置\")").click()
            driver.find_element_by_xpath('//android.widget.ImageButon[@content-desc=" "]').click()
            print('--->配网成功')
        except Exception:
            print('--->配网成功')

    # 进入设备（房间名，设备名）    
    def enter_the_device(self, room_name, devices_name):

        driver = self.driver
        driver.implicitly_wait(30)

        try:
            driver.find_element_by_android_uiautomator("text(\"%s\")" % room_name).click()
            driver.find_element_by_android_uiautomator("text(\"%s\")" % devices_name).click()
            print("--->进入%s中设备的控制界面" % room_name)
        except:
            driver.find_element_by_android_uiautomator("text(\"%s\")" % devices_name).click()
            print("--->进入%s的控制界面" % devices_name)

    # 删除设备（房间名）
    def delete_devices(self):
        print("--->开始删除设备")
        driver = self.driver
        driver.implicitly_wait(30)
        time.sleep(1)
        try:
            driver.find_element_by_xpath('(//android.widget.ImageButon[@content-desc=" "])[2]')

        except:
            driver.find_element_by_android_uiautomator("text(\"取消\")").click()

        finally:
            try:
                driver.find_element_by_xpath('(//android.widget.ImageButon[@content-desc=" "])[2]').click()
            except:
                TouchAction(driver).tap(x=981, y=182).perform()
            time.sleep(1)
            width = driver.get_window_size()['width']
            height = driver.get_window_size()['height']
            driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)  # 滑动屏幕
            time.sleep(0.2)
            driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2)
            time.sleep(0.2)
            driver.find_element_by_android_uiautomator("text(\"删除设备\")").click()
            driver.find_element_by_id('com.xiaomi.smarthome:id/button1').click()
            time.sleep(3)
            print("--->删除设备成功")

    # 退出米家app
    def mihome_close(self):
        self.driver.quit()
        print("--->已退出米家app")
        print("本次测试结束，已为您关闭米家app，感谢您的使用！")

# if __name__ == '__main__':
    