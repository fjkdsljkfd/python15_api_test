# -*- coding: utf-8 -*-#
# @Time :2019/4/2814:41
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :case_reports.py
import sys
sys.path.append("./")
print(sys.path)
import unittest
from API_7.conmon import cantins
import HTMLTestRunnerNew
discover = unittest.defaultTestLoader.discover(cantins.case_path,"test_*.py")
with open(cantins.reports_path + "/test.html","wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner( stream=file, verbosity=2, title="这是一个测试报告", description="有三个功能的测试报告")
    runner.run(discover)
