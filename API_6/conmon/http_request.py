# -*- coding: utf-8 -*-#
# @Time :2019/4/1513:43
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :http_request.py
import requests
from API_6.conmon.read_conf import Config
class HttpRquests:
    def __init__(self):
        self.session = requests.sessions.session()
    def http_res(self,method,url,data=None,json = None):
        url = Config().getvalue("url","pre_url")+url
        if type(data) == str:
            data = eval(data)
        if method.lower() == "get":
            resp = self.session.request(method,url,params=data)
        elif method.lower() == "post":
            if json:
                resp = self.session.request(method, url, json = json)
            else:
                resp = self.session.request(method,url,data = data)
        else:
            resp = None
            print("输入的请求方式不对")
        return resp
    def session_close(self):
        self.session.close()


