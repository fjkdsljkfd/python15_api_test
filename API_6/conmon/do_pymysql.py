# -*- coding: utf-8 -*-#
# @Time :2019/4/2210:26
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :do_pymysql.py
import pymysql
class DoMysql:
    def __init__(self):
        self.mysql = pymysql.connect(host = "test.lemonban.com",user = "test",password = "test",port = 3306)
        self.cursor = self.mysql.cursor()
    def fecth_one(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def fecth_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    def close_mysql(self):
        self.cursor.close()
        self.mysql.close()
if __name__ == '__main__':
    res = DoMysql().fecth_one("select max(mobilephone) from future.member")
    print(res)
