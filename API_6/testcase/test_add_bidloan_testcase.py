# -*- coding: utf-8 -*-#
# @Time :2019/4/1716:11
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :test_add_bidloan_testcase.py
import unittest
from API_3.conmon.http_request import HttpRquests
from API_6.conmon.read_write_excel import *
from ddt import ddt,data,unpack
from API_6.conmon import cantins
@ddt
class AddBidloan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRquests()
    @data(*ExcelTest(cantins.data_path,"addbidloan").read_excel())
    def test_add_bid(self,case):
        print(case.title)
        res = self.http_request.http_res(case.method,case.url,case.data).json()
        try:
            self.assertEqual(str(case.exp),res["code"])
        except AssertionError as e:
            ExcelTest(cantins.data_path, "addbidloan").write_excel(case.case_id+1,res["code"],"FAILD")
            raise e
        else:
            ExcelTest(cantins.data_path, "addbidloan").write_excel(case.case_id + 1, res["code"], "PASS")

    @classmethod
    def tearDownClass(cls):
        cls.http_request.session_close()
