# -*- coding: utf-8 -*-#
# @Time :2019/4/2210:42
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :context.py
import re
from API_6.conmon.read_conf import Config
def getdata(data):
    d = '#(.*?)#'
    while re.search(d,data):
        data_1 = re.search(d,data)
        data_2 = data_1.group(1)
        data_3 = Config().getvalue("login",data_2)
        data = re.sub(d,data_3,data,count = 1)
    return data
if __name__ == '__main__':
    data_haha = getdata('{"mobilephone":"register_mobilephone","pwd":"#password#","regna":"#name#"}')
    print(data_haha)