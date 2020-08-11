#！/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
import HTMLTestRunner
from lib.get_data import get_data
import os
from lib.send_email import send_email
from tester.user.test_add import *
from tester.user.test_add_group import *

if __name__ == '__main__':	
	# suite = unittest.TestSuite()
	# suite.addTests(unittest.TestLoader().loadTestsFromName('tester.user.test_add.TestAdd'))
	# suite.addTests(unittest.TestLoader().loadTestsFromName('tester.user.test_add_group.TestAddGroup'))
	base_path = os.path.dirname(__file__)
	testdir = os.path.join(base_path+"\\tester\\user\\")
	discover = unittest.defaultTestLoader.discover(testdir,"test*.py")
	#生成测试报告
	report_path = get_data("path","report_file")
	fp = open(report_path,"wb")
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'Api Test',description=u'用例执行情况',tester=u'fishyu')
	
	runner.run(discover)
	#runn.run(suite)
	fp.close()
	send_email() #将结果用邮件发送