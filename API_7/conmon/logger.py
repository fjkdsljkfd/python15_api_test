# -*- coding: utf-8 -*-#
# @Time :2019/4/2813:50
# @Author :xuqiao  
# @Email :1462942304@qq.com
# @File :logger.py
import logging
from API_7.conmon import cantins
from API_7.conmon.read_conf import Config
def logger(case):
    logger = logging.getLogger(case)
    logger.setLevel("INFO")
    console_hander = logging.StreamHandler()
    sonsole_level = Config().getvalue("data","console_level")
    console_hander.setLevel(sonsole_level)
    logger.addHandler(console_hander)
    fmt = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s-[%(filename)s-%(lineno)d]")
    console_hander.setFormatter(fmt)
    file_hander = logging.FileHandler(cantins.log_path + "/case.log",encoding="utf-8")
    file_level = Config().getvalue("data","filehander_level")
    file_hander.setLevel(file_level)
    file_hander.setFormatter(fmt)
    logger.addHandler(file_hander)
    return logger

if __name__ == '__main__':
    logger = logger("case")
    logger.info("这是测试用的")