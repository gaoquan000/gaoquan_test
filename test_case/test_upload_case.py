# -*- coding = utf-8 -*-
import time

import pytest

from common import driver, login_out
from common import get_log
from common import choose_space
from common import login
from common import import_case


@pytest.mark.flaky(reruns=2, reruns_delay=4)
# 上传文件
class TestUpLoad(object):

    def setup_class(self):
        url = "https://sale.xi-ai.com:23300/front/#/login"
        self.driver = driver.Driver.open_driver(url)
        self.log = get_log.GetLog().get_log_one()
        self.choose_space_one = choose_space.ChooseSpace(self.driver, self.log)
        self.login_one = login.Login(self.driver, self.log)
        self.import_one = import_case.ImportCase(self.driver, self.log)
        self.login_one.login_page()
        self.choose_space_one.choose_space()
        self.login_one.base_message()

    def test_upload_case01(self):
        shu_ju = self.import_one.upload_file("客户用户数据.xls")
        assert "上传成功" in shu_ju

    def test_upload_case02(self):
        shu_ju = self.import_one.upload_file("客户数据_cuowu.xls")
        assert "允许上传" in shu_ju

    def test_upload_case03(self):
        shu_ju = self.import_one.upload_file("数据emport.xls")
        assert "上传成功" not in shu_ju

    def teardown_class(self):
        time.sleep(2)
        login_out.LoginOut(self.driver, self.log).out_login()
        self.driver.close()


if __name__ == "__main__":
    TestUpLoad()
