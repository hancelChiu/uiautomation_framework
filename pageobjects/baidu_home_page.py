# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/8/6

from selenium.webdriver.common.by import By
from framework.base_page import BasePage
import sys
sys.path.append('../')


class BaiduPage(BasePage):
	'''
	定位页面元素
	'''
	search_loc = (By.ID, 'kw') #定位百度文本框
	click_btn = (By.ID, 'su') # 定位百度按钮
	news_link = (By.XPATH, "//*[@id='u1']/a[@name='tj_trnews']") # 百度新闻入口

	def input_text(self, text):
		self.send_key(self.search_loc, text)

	def click_baidu_btn(self):
		self.click(self.click_btn)

	def click_news(self):
		self.click(self.news_link)
		self.sleep(2)