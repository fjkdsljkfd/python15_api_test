# -*- coding: utf-8 -*-#
# @Time :2019/4/1714:05
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :test_invest_testcase.py
import unittest
from API_6.conmon.http_request import *
from API_6.conmon import cantins
from API_3.conmon.read_write_excel import *
from ddt import ddt,data,unpack
from API_6.conmon.context import getdata
@ddt
class BidLoanCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRquests()
    @data(*(ExcelTest(cantins.data_path,"bidLoan").read_excel()))
    def test_bidloan(self,case):
        case.data =getdata(case.data)
        print(case.data)
        res = self.http_request.http_res(case.method,case.url,case.data).json()
        try:
            self.assertEqual(str(case.exp),res["code"])
        except AssertionError as e:
            ExcelTest(cantins.data_path, "bidLoan").write_excel(case.case_id+1,res["code"],"FAILD")
            raise e
        else:
            ExcelTest(cantins.data_path, "bidLoan").write_excel(case.case_id + 1, res["code"], "PASS")

    @classmethod
    def tearDownClass(cls):
        cls.http_request.session_close()