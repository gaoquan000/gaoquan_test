# -*- coding = utf-8 -*-
import xlrd
import random
from xlutils.copy import copy

from common import get_log, get_element_file


class OperateExcel(object):

    def __init__(self):
        self.log = get_log.GetLog().get_log_one()

    def sui_ji(self):
        customer1 = "".join(random.sample("0123456789", 6))
        # customer2 = "".join(random.sample("0123456789", 5))
        # customer_id = "1" + customer1 + customer2
        return customer1

    def modify_info(self, file_path, upload_type):
        # wb = load_workbook(file_path)
        # sheet = wb["Sheet1"]
        wb = xlrd.open_workbook(file_path)
        wc = copy(wb)
        sheet = wc.get_sheet(0)
        if upload_type == "纯机":
            customer_id = self.sui_ji()
            sheet.write(1, 0, "0000-1111")
            sheet.write(1, 1, customer_id)
            sheet.write(1, 2, "测试电话")
            sheet.write(1, 3, "男")
            sheet.write(1, 4, "1501043468")
            sheet.write(1, 5, "纯机计划")
            wc.save(file_path)
            self.log.info("客户ID为：{}".format(customer_id))


if __name__ == "__main__":
    pass
    # path_two = get_element_file.GetElement().get_element("path", "path_info")
