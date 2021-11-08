# -*- coding: utf-8 -*-
import datetime
import os.path
import time

from common import get_element_file


class LoginOut(object):
    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
        self.element = get_element_file.GetElement(self.driver)

    def out_login(self):
        try:
            self.element.get_element("find_element", "seat_info").click()  # 点击个人信息
            self.element.get_element("find_element", "out").click()  # 点击退出登录
            self.log.info("退出登录成功")
            return True
        except Exception as e:
            self.log.error("退出登录失败{}".format(e))
            return False


if __name__ == "__main__":
    pass
