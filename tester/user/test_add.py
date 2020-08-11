#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
import requests
import json
import os
import sys
sys.path.append("../..")
from lib.read_excel import excel_to_list,get_test_data
from lib.log import *
from lib.get_data import get_data



class TestAdd(unittest.TestCase):
	def setUp(self):
		data_file = get_data("path","data_file")            #获取数据文件
		auth_user = get_data("server","auth_user")          #获取登录用户名
		auth_password = get_data("server","auth_password")  #获取登录密码
		self.url = get_data("server","url_users")           #获取url
		self.auth = (auth_user,auth_password)
		self.data_list = excel_to_list(data_file,"Sheet1")

	#新增正常用户
	def test_add_normal(self):
		case_data = get_test_data(self.data_list,"test_add_normal")  #获取test_add_normal用例数据
		if not case_data:
			logging.error("用例数据不存在")
		form_data = case_data.get("data")  #从用例中获取data数据
		try:
			#form_data = {'username':'nor01','email':'101010@33.com'}
			r = requests.post(url=self.url,data=json.loads(form_data),auth=self.auth)
			result = r.json()
			self.assertEqual(result['username'],'nor005')
		except Exception as e:
			logging.error(str("test_add_normal：新增用户已存在，无法添加"))
			#print(e)

	#新增时缺少必填项username
	def test_add_wrong(self):
		case_data = get_test_data(self.data_list,"test_add_wrong")
		if not case_data:
			logging.error("用例数据不存在")
		form_data = case_data.get("data")
		#form_data = {'email':'202020@11.com'}
		r = requests.post(url=self.url,data=json.loads(form_data),auth=self.auth)
		result = r.json()
		self.assertEqual(r.status_code,400)

	#新增时email传入非法值
	def test_add_valid(self):
		case_data = get_test_data(self.data_list,"test_add_valid")
		if not case_data:
			logging.error("用例数据不存在")
		form_data = case_data.get("data")
		#form_data = {'username':'22222','email':'33333','groups':'http://localhost:8000/group/2/'}
		r = requests.post(url=self.url,data=json.loads(form_data),auth=self.auth)
		result = r.json()
		self.assertEqual(r.status_code,400)

	#新增时没有传入参数
	def test_add_null(self):
		case_data = get_test_data(self.data_list,"test_add_null")
		if not case_data:
			logging.error("用例数据不存在")
		form_data = case_data.get("data")
		#form_data = {}
		r = requests.post(url=self.url,data=json.loads(form_data),auth=self.auth)
		result = r.json()
		self.assertEqual(r.status_code,400)

if __name__ == '__main__':
	unittest.main()