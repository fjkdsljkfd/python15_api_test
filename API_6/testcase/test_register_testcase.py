# -*- coding: utf-8 -*-#
# @Time :2019/4/1514:57
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :test_register_testcase.py
import unittest
from API_6.conmon.read_write_excel import *
from API_6.conmon.http_request import HttpRquests
from API_6.conmon import cantins
from ddt import ddt,data,unpack
from API_6.conmon.do_pymysql import DoMysql
from API_6.conmon.context import getdata
@ddt
class RegisterTestcase(unittest.TestCase):
    doexcel = ExcelTest(cantins.data_path, "register")
    case = doexcel.read_excel()
    @classmethod
    def setUpClass(cls):
        cls.session = HttpRquests()
    def setUp(self):
        self.mysql = DoMysql()
    @data(*case)
    def test_register(self,case):
        if case.data.find("register_mobilephone")>-1:
            res_data = self.mysql.fecth_one("select max(mobilephone) from future.member")
            print(res_data)
            data_2 = str(int(res_data[0])+1)
            case.data = case.data.replace("register_mobilephone",data_2)
            print(case.data)
        case.data = getdata(case.data)
        print(case.data)
        res = self.session.http_res(case.method,case.url,case.data).text
        try:
            self.assertEqual(case.exp,res)
        except AssertionError as e:
            self.doexcel.write_excel(case.case_id + 1, res, "FIAL")
            raise e
        else:
            self.doexcel.write_excel(case.case_id + 1, res, "PASS")
    def tearDown(self):
        self.mysql.close_mysql()
    @classmethod
    def tearDownClass(cls):
        cls.session.session_close()