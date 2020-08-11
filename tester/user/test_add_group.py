#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
import requests
import os
import sys
sys.path.append("../..")
import json
from lib.log import *
from lib.get_data import get_data
from lib.read_excel import excel_to_list,get_test_data

class TestAddGroup(unittest.TestCase):
	def setUp(self):
		#获取URL、用户名、密码、数据文件
		self.url_groups = get_data("server","url_groups")
		auth_user = get_data("server","auth_user")
		auth_password = get_data("server","auth_password")
		data_file = get_data("path","data_file")
		sheet_name = get_data("path","sheet_name")
		#进入群组页面
		self.auth = (auth_user,auth_password)
		self.data_list = excel_to_list(data_file,sheet_name)

	#新建正常groups
	def test_add_groups_normal(self):
		#获取需要使用的数据
		case_data = get_test_data(self.data_list,"test_add_groups_normal")
		#判断数据是否为空
		if not case_data:
			logging.error("用例数据不存在")
		form_data = case_data.get("data")  #从用例中获取数据
		#判断用户是否存在，不存在新增，存在退出
		try:
			r = requests.post(url=self.url_groups,data=json.loads(form_data),auth=self.auth)
			result = r.json()
			self.assertEqual(result["name"],"test02")
		except Exception as e:
			logging.error("用户已存在")

	#新增时数据未NUll
	def test_add_groups_null(self):
		#获取需要使用的数据
		case_data = get_test_data(self.data_list,"test_add_groups_null")
		#判断数据是否为空
		if not case_data:
			logging.error("用例数据不存在")
		form_data = case_data.get("data")
		r = requests.post(url=self.url_groups,data=json.loads(form_data),auth=self.auth)
		result = r.json()
		self.assertEqual(r.status_code,400)

if __name__ == '__main__':
	unittest.main()


