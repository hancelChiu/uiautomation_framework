# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/8/5

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from configparser import ConfigParser
import os
import getpathInfo
from framework.logger import Logger

logger = Logger(logger="BrowserDriver").get_logger()

pro_dir = getpathInfo.get_path()
class BrowserDriver(object):

	driver_path = pro_dir + '/tools/'
	chrome_driver_path = driver_path + "chromedriver.exe"
	ie_driver_path = driver_path + "IEDriverServer.exe"
	firefox_driver_path = "geckodriver.exe"
	def __init__(self, driver):
		self.driver = driver

	def open_browser(self,driver):
		config = ConfigParser()
		file_path = os.path.join(pro_dir + '/config/config.ini')
		config.read(file_path)

		browser = config.get("browserType", "browserName")
		logger.info("选择的浏览器为 {}".format(browser))
		url = config.get("testServer","URL")
		logger.info("打开的URL为：{}".format(url))

		if browser == "Firefox":
			driver = webdriver.Firefox()
			logger.info("启动火狐浏览器")
		elif browser == "Chrome":
			driver = webdriver.Chrome(self.chrome_driver_path)
			logger.info("启动谷歌浏览器")
		elif browser == "IE":
			driver = webdriver.Ie(self.ie_driver_path)
			logger.info("启动IE浏览器")
		driver.get(url)
		driver.maximize_window()
		driver.implicitly_wait(5)
		logger.info("设置5秒隐式等待时间")
		return driver

	def quit_browser(self):
		self.driver.quit()
