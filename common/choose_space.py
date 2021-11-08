# -*- coding = utf-8 -*-
import time

from common import get_element_file
from common import driver, get_log, login, import_case, login_out


class ChooseSpace(object):
    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
        self.element = get_element_file.GetElement(driver)

    def choose_space(self):
        self.driver.implicitly_wait(3)
        space = self.element.get_element("element", "admin")
        try:
            self.driver.find_element_by_xpath(
                "//*[@id='app']/div/div/main/main/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[1]/span").click()
            self.log.info("进入空间：{}".format(space))
            # self.driver.find_element_by_css_selector(space).click()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    path = "https://sale.xi-ai.com:23300/front/#/login"
    log = get_log.GetLog().get_log_one()
    driver = driver.Driver.open_driver(path)
    login.Login(driver, log).login_page()
    ChooseSpace(driver, log).choose_space()
    login.Login(driver, log).base_message()
    driver.implicitly_wait(5)
    # import_case.ImportCase(driver, log).upload_file()
    login_out.LoginOut(driver, log).out_login()