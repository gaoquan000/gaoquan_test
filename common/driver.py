# -*- coding = utf-8 -*-
from selenium import webdriver
from common import get_log
from common import get_element_file
from common import login

class Driver(object):

    # 打开浏览器
    @staticmethod
    def open_driver(url):
        opt = webdriver.ChromeOptions()
        # 设置下载路径
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_settings.popups": 0,
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1,
        }
        # 允许访问麦克风，并关闭记住密码
        opt.add_argument("--disable-infobars")
        opt.add_argument("--start-maximized")
        opt.add_argument("--disable-popup-blocking")
        opt.add_argument("no-sandbox")
        opt.add_argument("disable-extensions")
        opt.add_argument("no-default-browser-check")
        # 关闭各种提示
        opt.add_experimental_option("prefs", prefs)
        # 关闭左上方 Chrome 正受到自动测试软件的控制的提示
        opt.add_experimental_option("excludeSwitches", ['enable-automation'])
        # 无界面启动浏览器
        opt.headless = True
        driver = webdriver.Chrome(options=opt)
        driver.get(url=url)
        # driver.set_window_size(1920,1080)
        driver.maximize_window()
        get_log.GetLog().get_log_one().info("浏览器启动成功")
        return driver


if __name__ == "__main__":
    path = "https://sale.xi-ai.com:23300/front/#/login"
    driver = Driver.open_driver(path)
    log = get_log.GetLog().get_log_one()
    username = get_element_file.GetElement(driver).get_element("element", "username")
    password = get_element_file.GetElement(driver).get_element("element", "password")
    driver.find_element_by_id("userName").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_css_selector(
        "#app > section > main > div.login_area > form > div:nth-child(3) > div > div > span > button").click()
    login.Login(driver, log).choose_space()
