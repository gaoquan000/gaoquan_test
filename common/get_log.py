# -*- coding = utf-8 -*-
import logging
import os


class GetLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.handlers.clear()
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__))+"/logs/zidong.log")
        # path3 = os.path.dirname(os.path.dirname(__file__))
        self.log_handle = logging.FileHandler(self.path, encoding="utf-8")  # 打开流

    def get_log_one(self):
        formatter = logging.Formatter(
            "%(asctime)s-->%(filename)s %(funcName)s %(lineno)s-->%(levelname)s %(message)s"
        )
        self.log_handle.setFormatter(formatter)
        self.logger.addHandler(self.log_handle)
        return self.logger

    def control_log(self):
        control_handle = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s---->%(filename)s %(funcName)s %(lineno)s---->%(levelname)s %(message)s"
        )
        control_handle.setFormatter(formatter)
        self.logger.addHandler(control_handle)
        return self.logger


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + "/config/config.ini")
    GetLog().control_log().info("控制台")
