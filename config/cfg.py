#/usr/bin/env python
#-*- coding:utf-8 -*-

import logging
import os

# 项目路径
prj_path = os.path.dirname(os.path.abspath(__file__))  # 当前文件的绝对路径的上一级，__file__指当前文件

data_file = os.path.join(prj_path,'data','data.xlsx')  # 数据目录，暂时在项目目录下
test_path = os.path.join(prj_path,'test')  # 用例目录，暂时在项目目录下

log_file = os.path.join(prj_path,'log',"log.txt")  # 也可以每天生成新的日志文件
report_file = os.path.join(prj_path,'report',"report.html")  # 也可以每次生成新的报告

#email
from_addr = "13554935131@163.com" 
to_addr = "971234452@qq.com"
smtp_server = "smtp.163.com"
smtp_port = 25
from_password = "Yuweitao123"