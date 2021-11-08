# -*- coding = utf-8 -*-
import os

from common import get_element_file


class Login(object):
    def __init__(self, driver, log):
        self.log = log
        self.element = get_element_file.GetElement(driver)
        self.driver = driver

    def login_page(self):
        username = self.element.get_element("element", "username")
        password = self.element.get_element("element", "password")
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_css_selector(
            "#app > section > main > div.login_area > form > div:nth-child(3) > div > div > span > button").click()
        self.log.info("登录成功")
        return None

    def choose_space(self):
        space = self.element.get_element("element", "admin")
        css_element = self.element.get_element("element", "space_element")
        if space == "测试复制FS空间":
            try:
                self.driver.find_element_by_xpath(css_element).click()
                self.log.info("进入空间{}".format(space))
            except Exception as e:
                self.log.error(e)
        else:
            self.log.info("未找到测试空间{}".format(space))

    def base_message(self):
        try:
            value = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/div[1]/ul/li[1]/span[2]')
            value.click()
            self.driver.implicitly_wait(3)
            self.log.info("进入客户中心")
        except Exception as e:
            print(e)

    def upload(self):
        self.driver.find_element_by_class_name("btn_no_border hz_margin ant-btn").click()
        upload_path = "客户用户数据.xls"
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/span/div[1]/span/input").send_keys(upload_path)
        self.driver.find_element_by_class_name("ant-btn ant-btn-primary").click()

    @staticmethod
    def sort_file(file_path):
        dir_list = os.listdir(file_path)
        if not dir_list:
            return
        else:
            # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
            # os.path.getmtime() 函数是获取文件最后修改时间
            # os.path.getctime() 函数是获取文件最后创建时间
            dir_list = sorted(dir_list, key=lambda x: os.path.getctime(os.path.join(file_path, x)), reverse=False)
            # print(dir_list)
            return dir_list


if __name__ == "__main__":
    path = os.path.dirname(os.path.dirname(__file__))
    last_path = os.path.join(path + '/report')
    Login.sort_file(last_path)
