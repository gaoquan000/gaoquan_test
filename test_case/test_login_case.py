# -*- coding = utf-8 -*-
import time

from common import driver, login_out
from common import get_log
from common import choose_space
from common import login
from common import import_case


# 测试登录
# TODO:登录测试用例编写
class DengLu(object):

    def setup_class(self):
        url = "234"
        self.driver = driver.Driver.open_driver(url)
        self.log = get_log.GetLog().get_log_one()
        pass

    def test_l0gin_case01(self):
        pass

    def test_login_case02(self):
        pass

    def teardown_class(self):
        pass