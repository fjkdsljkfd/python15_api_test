# -*- coding: utf-8 -*-#
# @Time :2019/4/1711:03
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :test_login_testcase.py
import unittest
from ddt import ddt,data,unpack
from API_6.conmon.http_request import HttpRquests
from API_6.conmon.read_write_excel import *
from API_6.conmon import cantins
from API_6.conmon.context import getdata

@ddt
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRquests()
    @data(*ExcelTest(cantins.data_path,"login").read_excel())
    def test_logintest(self,case):
        case.data = getdata(case.data)
        res = HttpRquests().http_res(case.method,case.url,case.data).text
        try:
            self.assertEqual(case.exp,res)
        except AssertionError as e:
            ExcelTest(cantins.data_path,"login").write_excel(case.case_id+1,res,"FAIL")
        else:
            ExcelTest(cantins.data_path,"login").write_excel(case.case_id+1,res,"PASS")
    @classmethod
    def tearDownClass(cls):
        cls.http_request.session_close()



