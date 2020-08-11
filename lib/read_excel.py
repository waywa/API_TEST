#!/usr/bin/env python
#-*- coding:utf-8 -*-

import xlrd


# wb = xlrd.open_workbook('data.xlsx')
# sh = wb.sheet_by_name('Sheet1')
# print(sh.nrows)
# print(sh.ncols)
# print(sh.cell(0,0).value)
# print(sh.row_values(0))

# print(dict(zip(sh.row_values(0),sh.row_values(2))))

# #打印所有数据
# for i in range(sh.nrows):
# 	print(sh.row_values(i))

def excel_to_list(data_file,sheet):
	data_list = [] #新建一个空的list来装所有数据
	wb = xlrd.open_workbook(data_file) #打开excel
	sh = wb.sheet_by_name(sheet) #获取sheet表
	header = sh.row_values(0) #获取行标
	for i in range(1,sh.nrows):
		d = dict(zip(header,sh.row_values(i))) #将标题和每行数据组装成字典
		data_list.append(d)
	return data_list  #列表嵌套字典格式，每个元素是一个字典

def get_test_data(data_list,case_name):
	for case_data in data_list:
		if case_name == case_data['case_name']:   #如果字典中case_name与参数一致
			return case_data

if __name__ == '__main__':
	data_list = excel_to_list('E:\\python接口自动化测试文件\\API_Auto_Test\\data\\data.xlsx','Sheet1')
	case_data = get_test_data(data_list,"test_add_normal")
	print(case_data)
