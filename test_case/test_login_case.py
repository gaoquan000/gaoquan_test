# -*- coding = utf-8 -*-
import time

from common import driver, login_out, get_element_file
from common import get_log
from login import page_login
from common import choose_space
from common import login
from common import import_case


# 测试登录
# TODO:登录测试用例编写
class TestDengLu(object):

    def setup_class(self):
        # url = get_element_file.GetElement().get_element("element", "path")
        url = "https://sale.xi-ai.com:23300/front/#/login"
        self.driver = driver.Driver.open_driver(url)
        self.log = get_log.GetLog().get_log_one()
        self.login = page_login.PageLogin(self.driver, self.log)

    def test_login_case01(self):
        actual, expect = self.login.sign_in(1)
        assert expect == actual

    def test_login_case02(self):
        actual, expect = self.login.sign_in(2)
        assert expect == actual

    def test_login_case03(self):
        actual, expect = self.login.sign_in(3)
        assert expect == actual

    def test_login_case04(self):
        actual, expect = self.login.sign_in(4)
        assert expect == actual

    def test_login_case05(self):
        actual, expect = self.login.sign_in(5)
        assert expect == actual

    def test_login_case06(self):
        actual, expect = self.login.sign_in(6)
        assert expect == actual

    def test_login_case07(self):
        actual, expect = self.login.sign_in(7)
        assert expect == actual

    def teardown_class(self):
        self.driver.close()


if __name__ == "__main__":
    TestDengLu()
