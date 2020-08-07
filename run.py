# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/8/6

import unittest
from framework import HTMLTestRunner
import time
import getpathInfo
from framework.read_config import ReadConfig
from framework.send_email import SendEmail
from framework.logger import Logger

pro_dir = getpathInfo.get_path()
on_off = ReadConfig().get_email("on_off")
log = Logger(logger='AllTest').get_logger()


class AllTest():

	def set_case_suite(self):
		testsuite = unittest.TestSuite()
		test_dir = pro_dir+'/testsuites/'

		discover = unittest.defaultTestLoader.discover(
			start_dir=test_dir,
			pattern='test*.py',
			top_level_dir=None)
		for test_case in discover:
			testsuite.addTest(test_case)
		return testsuite


	def run(self):
		now = time.strftime("%Y-%m-%d_%H_%M_%S_")
		report_name = pro_dir + '/test_report/' + now + 'result.html'
		try:
			suit = self.set_case_suite()
			if suit is not None:

				fp = open(report_name, 'wb')
				runner = HTMLTestRunner.HTMLTestRunner(
					stream=fp,
					title="测试报告",
					description="测试用例执行情况"
				)
				runner.run(suit)
				fp.close()
			else:
				print("Have no case to test.")
		except Exception as e:
			print(str(e))
		finally:
			print("*"*5 + "TEST END" + "*"*5)
		if on_off == "on":
			SendEmail().send_email(report_name)
		else:
			print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")

if __name__ =="__main__":
	AllTest().run()