# -*- coding: utf-8 -*-#
# @Time :2019/4/1816:14
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :test_audit_testcase.py
import unittest
from API_6.conmon.http_request import HttpRquests
from API_6.conmon import cantins
from API_3.conmon.read_write_excel import *
from ddt import ddt,data,unpack
@ddt
class AuditCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.http_resquest = HttpRquests()
    @data(*ExcelTest(cantins.data_path,"audit").read_excel())
    def test_audit(self,case):
        print(case.title)
        res = self.http_resquest.http_res(case.method,case.url,case.data).json()
        try:
            self.assertEqual(str(case.exp),res["code"])
        except AssertionError as e:
            ExcelTest(cantins.data_path, "audit").write_excel(case.case_id+1,res["code"],"FAILD")
            raise e
        else:
            ExcelTest(cantins.data_path, "audit").write_excel(case.case_id + 1, res["code"], "PASS")
    @classmethod
    def tearDownClass(cls):
        cls.http_resquest.session_close()
