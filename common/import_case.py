# -*- coding = utf-8 -*-
import time
from selenium.webdriver.support.wait import WebDriverWait
from common import get_element_file, get_log, modify_excle
import xlrd
import random
from xlutils.copy import copy


class ImportCase(object):
    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
        self.element = get_element_file.GetElement(driver)

    def upload_file(self, path_two):
        time.sleep(3)
        self.path_two = path_two
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/main/div[1]/button[1]').click()
        path_one = self.element.get_element("path", "path_info")
        upload_path = path_one + self.path_two
        self.driver.implicitly_wait(3)
        # modify_excle.OperateExcel().modify_info(upload_path, "纯机")
        # self.driver.find_element_by_css_selector("input[type=file]").send_keys(upload_path)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/span/div[1]/span/input').send_keys(upload_path)
        self.driver.find_element_by_css_selector('.ant-btn-primary:nth-child(2)').click()
        try:
            tip = self.driver.find_element_by_css_selector(
                ".ant-message-custom-content > span:nth-child(2)").get_attribute("textContent")
            self.log.info(tip)
        except Exception as e:
            self.log.info("没有定位到提示")
            tip = '失败'
        time.sleep(1)
        try:
            # self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[1]').click()
            self.driver.find_element_by_css_selector("div.ant-modal-footer>div>button:nth-child(1)").click()
        except:
            self.log.info("成功导入数据")
        else:
            self.log.info("取消导入")
        return tip



if __name__ == "__main__":
    pass
