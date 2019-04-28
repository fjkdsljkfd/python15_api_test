# -*- coding: utf-8 -*-#
# @Time :2019/4/1710:18
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :read_conf.py
from configparser import ConfigParser
from API_6.conmon import cantins
class Config:
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(cantins.global_path)
        switch = self.cf.getboolean("global","on")
        if switch:
            self.cf.read(cantins.test_url_path,encoding = "utf-8")
        else:
            self.cf.read(cantins.online_url_path,encoding = "utf-8")
    def getvalue(self,section,option):
        return self.cf.get(section,option)
if __name__ == '__main__':
    res = Config().getvalue("user_info","password")
    print(res)
