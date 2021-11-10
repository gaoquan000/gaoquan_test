# -*- coding = utf-8 -*-
import configparser
import os
from common import get_log


class GetElement(object):
    def __init__(self, driver_one = None):
        self.driver_one = driver_one
        self.log = get_log.GetLog().get_log_one()
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + "/config/config.ini")  # 配置文件路径
        self.config = configparser.ConfigParser()
        self.config.read(self.path, encoding="utf-8")  # 读取配置文件放在控制台中

    def get_element(self, section, option):
        try:
            data_dy = self.config.get(section, option)
            by = data_dy.split("|")[0]
            data_one = data_dy.split("|")[1]
            if by == "no":
                return data_one
            elif by == "xpath":
                return self.driver_one.find_element_by_xpath(data_one)
            elif by == "css":
                return self.driver_one.find_element_by_css_selector(data_one)
            else:
                self.log.info("未找到元素")
        except Exception as error:
            self.log.info(error)

    def modify_element(self, section, option, value):
        self.config.set(section, option, value)
        self.config.write(open(self.path, "w"))


if __name__ == "__main__":
    driver = 12
    data = GetElement(driver).get_element("find_element", "out")

