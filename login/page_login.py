# -*- coding = utf-8 -*-
import time

from common import get_log, get_element_file, driver
import xlrd
from xlutils.copy import copy


class PageLogin(object):
    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
        self.element = get_element_file.GetElement(driver)

    def write_data(self, a, b):
        file_path = self.element.get_element('find_element', 'login_file')
        wb = xlrd.open_workbook(file_path)          # 打开工作簿
        wc = copy(wb)
        sheet = wc.get_sheet(0)  # 定位表
        sheet.write(a, b, "0000-1111")  # 写入数据
        self.log.info("写入成功")

    def get_data(self, a):
        file_path = self.element.get_element('find_element', 'login_file')
        # file_path = "./登录信息.xlsx"
        wb = xlrd.open_workbook(file_path)
        data = wb.sheet_by_index(0)
        account = data.cell_value(a, 0)
        password = data.cell_value(a, 1)
        expect = data.cell_value(a, 2)
        self.log.info("测试账号是：{}，测试密码是：{}".format(account, password))
        return account, password, expect

    def data_login(self, account, password, expect):
        self.driver.find_element_by_css_selector('input[type="text"]').clear()
        self.driver.find_element_by_css_selector('input[type="text"]').send_keys(account)
        self.driver.find_element_by_css_selector('input[type="password"]').clear()
        self.driver.find_element_by_css_selector('input[type="password"]').send_keys(password)
        self.driver.find_element_by_css_selector('.ant-btn').click()
        self.log.info("登录")
        self.driver.implicitly_wait(1)
        try:
            tip = self.driver.find_element_by_css_selector(
                '.ant-message-custom-content > span:nth-child(2)').get_attribute("textContent")
        except Exception as e:
            self.log.error("获取提示失败：{}".format(e))
        else:
            self.log.info("登录失败：{}".format(tip))
            self.log.info("实际结果：{},预期结果：{}".format(tip, expect))
            return tip, expect
        try:
            tip = self.driver.find_element_by_css_selector(
                '.ant-form>div:nth-child(1)>.ant-col>.ant-form-item-control>.ant-form-explain').get_attribute("textContent")
        except Exception as e:
            self.log.info("没有获取到提示：{}".format(e))
        else:
            self.log.info("登录失败：{}".format(tip))
            self.log.info("实际结果：{},预期结果：{}".format(tip, expect))
            return tip, expect
        try:
            tip = self.driver.find_element_by_css_selector(
                '.ant-form>div:nth-child(2)>.ant-col>.ant-form-item-control>.ant-form-explain').get_attribute("textContent")
        except Exception as e:
            # self.log.info("没有获取提示或者获取提示失败：{}".format(e))
            self.log.info("登录成功")
            tip = "登录成功"
            return tip, expect
        else:
            self.log.info("登录失败：{}".format(tip))
            self.log.info("实际结果：{},预期结果：{}".format(tip, expect))
            return tip, expect

    def sign_in(self, n):
        account, password, expect = self.get_data(n)
        tip, expect = self.data_login(account, password, expect)
        time.sleep(5)
        return tip, expect


if __name__ == "__main__":
    url = "https://sale.xi-ai.com:23300/front/#/login"
    driver = driver.Driver().open_driver(url)
    log = get_log.GetLog().get_log_one()
    a, b = PageLogin(driver, log).sign_in(1)
    print(a, b)
