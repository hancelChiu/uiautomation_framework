# -*- coding: utf-8 -*-
# _author:"hancel"
# date:2020/8/6
import unittest
import paramunittest
from framework.browser_driver import BrowserDriver
from pageobjects.baidu_home_page import BaiduPage
from framework.read_excel import ReadExcel


data = ReadExcel().get_xls('data.xlsx', 'Sheet1')
@paramunittest.parametrized(*data)

class BaiduSearch(unittest.TestCase):

	def setParameters(self, data):
		self.data = data

	@classmethod
	def setUpClass(cls):
		browser = BrowserDriver(cls)
		cls.driver = browser.open_browser(cls)

	def test_baidu_search(self):
		baidu_page = BaiduPage(self.driver)
		baidu_page.input_text(self.data)
		baidu_page.click_baidu_btn()
		baidu_page.sleep(2)
		baidu_page.get_screenshots()
		try:
			assert self.data in baidu_page.get_title()
			print("Test Pass.")
		except Exception as e:
			print('Test Fail.', format(e))

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()


if __name__ == "__main__":
	unittest.main()
