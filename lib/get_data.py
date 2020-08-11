#!/usr/bin/env python
#-*- coding:utf-8 -*-

import configparser
import os

#获取配置文件路径
# pwd = os.getcwd()   #获取当前文件路径
# garder = os.path.dirname(pwd)  #获取当前文件的父目录
# cfg = os.path.join(garder+"\\config\\config.conf")  #父目录下进去配置文件夹下

def get_data(title,data):
	#读取配置文件数据
	cfg = "E:\\python接口自动化测试文件\\API_Auto_Test\\config\\config.conf"
	cp = configparser.ConfigParser()
	cp.read(cfg,encoding="utf-8")
	result = cp.get(title,data) #根据配置文件的标题+参数名获取参数
	return result

if __name__ == '__main__':
	print(get_data("mail","server"))
	print(get_data("path","data_file"))
