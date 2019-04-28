# -*- coding: utf-8 -*-#
# @Time :2019/4/2413:38
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :test_recharge_testcase.py
import unittest
from API_6.conmon.do_pymysql import DoMysql
from API_6.conmon import cantins
from API_6.conmon.read_write_excel import *
from API_6.conmon.context import getdata
from API_6.conmon.http_request import HttpRquests
from ddt import ddt,data,unpack
@ddt
class Recharge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.session = HttpRquests()
    def setUp(self):
        self.mysql = DoMysql()
    @data(*ExcelTest(cantins.data_path,"recharge").read_excel())
    def test_recharge(self,case):
        case.data = getdata(case.data)
        res = self.session.http_res(case.method,case.url,case.data).json()
        try:
            self.assertEqual(str(case.exp),res["code"])
            ExcelTest(cantins.data_path, "recharge").write_excel(case.case_id+1,res["code"],"PASS")
            if case.case_id == 3:
                self.mysql.fecth_one("select id from future.loan where ")
        except AssertionError as e:
            ExcelTest(cantins.data_path, "recharge").write_excel(case.case_id + 1, res["code"], "FILE")
    def tearDown(self):
        self.mysql.close_mysql()
    @classmethod
    def tearDownClass(cls):
        cls.session.session_close()