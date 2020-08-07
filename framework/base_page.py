# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/8/5

import time
from selenium.common.exceptions import NoSuchElementException
import os,sys
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import getpathInfo

logger = Logger(logger="BasePage").get_logger()

class BasePage():
	'''
	定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法
	'''
	def __init__(self, driver):
		self.driver = driver
		self.pro_path = getpathInfo.get_path()


	# 退出浏览器
	def quit_browser(self):
		self.driver.quit()

	# 浏览器前进操作
	def forward(self):
		self.driver.forward()

	# 浏览器后退
	def back(self):
		self.driver.back()

	# 隐式等待
	def wait(self, seconds):
		self.driver.implicitly_wait(seconds)
		logger.info("等待 %d秒."%seconds)
	@staticmethod
	def sleep(seconds):
		time.sleep(seconds)

	# 点击关闭当前窗口
	def close(self):
		try:
			self.driver.close()
			logger.info("关闭浏览器窗口.")
		except NameError as e:
			logger.error("关闭浏览器窗口失败 {}".format(e))

	# 退出浏览器
	def quit(self):
		self.driver.quit()

	# 保存图片
	def get_screenshots(self):
		file_path = os.path.join(self.pro_path +  '/screenshots/')
		now = time.strftime('%Y-%m-%d %H%M%S', time.localtime(time.time()))
		screen_name = file_path + now + '.png'
		try:
			self.driver.get_screenshot_as_file(screen_name)
			logger.info("页面已截图，截图的路径在:{}".format(file_path))
		except NameError as ne:
			logger.error("失败截图 {}".format(ne))
			self.get_screenshots()


	# 定位元素方法
	def find_element(self, *loc):
		try:
			# 元素可见时，返回查找到的元素
			WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element(*loc).is_displayed())
			return self.driver.find_element(*loc)
		except NoSuchElementException:
			logger.error("找不到定位元素{}".format(loc[1]))
			raise
		except TimeoutError:
			logger.warning('查找元素超时：{}'.format(loc[1]))
			raise

	def find_elements(self, *loc):
		try:
			# 元素可见时，返回查找到的元素
			WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_elements(*loc).is_displayed())
			return self.driver.find_elements(*loc)
		except NoSuchElementException:
			logger.error("找不到定位元素{}".format(loc[1]))
			raise
		except TimeoutError:
			logger.warning('查找元素超时：{}'.format(loc[1]))
			raise

	# 发送文本
	def send_key(self, loc, text):
		logger.info("清空文本框内容{}".format(loc[1]))
		self.find_element(*loc).clear()
		time.sleep(1)
		logger.info("输入内容{}".format(text))
		try:
			self.find_element(*loc).send_keys(text)
			time.sleep(2)
		except Exception as e:
			logger.error("输入内容失败{}".format(e))
			self.get_screenshots()

	# 点击
	def click(self, loc):
		try:
			self.find_element(*loc).click()
			time.sleep(2)
		except AttributeError as e:
			logger.error("无法点击元素{}".format(e))
			raise

	# 鼠标悬停操作
	def move_to_element(self,loc):
		element = self.find_element(*loc)
		ActionChains(self.driver).move_to_element(element).perform()

	# 获取title
	def get_title(self):
		return self.driver.title

	# 获取文本
	def get_text(self,loc):
		element = self.find_element(*loc)
		return element.text

	# 获取属性
	def get_attribute(self,loc,name):
		element = self.find_element(*loc)
		return element.get_attribute(name)

	# 执行js
	def js_execute(self,js):
		return self.driver.execute_script(js)

	# 聚焦元素
	def js_focus_element(self,loc):
		target = self.find_element(*loc)
		self.driver.execute_script("arguments[0].scrollIntoView();", target)

	# 滚动到顶部
	def js_scroll_top(self):
		js = "windows.scrollTo(0,0)"
		self.driver.execute_script(js)

	# 滚动到底部
	def js_scroll_end(self):
		js = "windows.scrollTo(0,document.body.scrollHeight)"
		self.driver.execute_script(js)

	# 下拉列表定位
	# 通过索引
	def select_by_index(self, loc, index):
		element = self.find_element(*loc)
		Select(element).select_by_index(index)

	# 通过value属性
	def select_by_value(self, loc, value):
		element = self.find_element(*loc)
		Select(element).select_by_value(value)

	# 通过文本值
	def select_by_text(self, loc, text):
		element = self.find_element(*loc)
		Select(element).select_by_visible_text(text)

	# 判断文本在元素里
	def is_text_in_element(self,loc,text, timeout=10):
		try:
			result = WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(loc, text))
		except TimeoutException:
			print("元素没有定位到：" + str(loc))
			return False
		else:
			return result

	def is_value_in_element(self,loc,value,timeout=10):
		'''
		判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        result = driver.text_in_element(element, text)
		:param loc:
		:param value:
		:param timeout:
		:return:
		'''
		try:
			result = WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element_value(loc,value))
		except TimeoutException:
			print("元素没定位到："+str(loc))
			return False
		else:
			return result

	def is_title(self,title, timeout=10):
		'''
		判断title完全等于
		:param title:
		:param timeout:
		:return:
		'''
		result = WebDriverWait(self.driver,timeout,1).until(EC.title_is(title))
		return result

	def is_title_contains(self,title,timeout=10):
		'''
		判断title包含
		:param title:
		:param timeout:
		:return:
		'''
		result = WebDriverWait(self.driver, timeout,1).until(EC.title_contains(title))
		return result

	def is_selected(self,loc, timeout=10):
		'''
		判断元素被选中，返回布尔值
		:param loc:
		:param timeout:
		:return:
		'''
		result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_to_be_selected(loc))
		return result

	def is_selected_be(self,loc,selected=True,timeout=10):
		'''判断元素的状态，selected是期望的参数true/false， 返回布尔值'''
		result = WebDriverWait(self.driver,timeout,1).until(EC.element_located_selection_state_to_be(loc,selected))
		return result

	def is_alert_present(self, timeout=10):
		'''
		判断页面是否有alert,如果有返回alert,没有返回false
		:param timeout:
		:return:
		'''
		result = WebDriverWait(self.driver, timeout,1).until(EC.alert_is_present())
		return result

	def is_visibility(self,loc,timeout=10):
		'''
		元素可见返回本身，不可见返回false
		:param loc:
		:param timeout:
		:return:
		'''
		result = WebDriverWait(self.driver, timeout,1).until(EC.visibility_of_element_located(loc))
		return result

	def is_invisibility(self,loc,timeout=10):
		'''
		元素可见返回本身，不可见返回True,没找到也返回True
		:param loc:
		:param timeout:
		:return:
		'''
		result = WebDriverWait(self.driver,timeout,1).until(EC.invisibility_of_element_located(loc))
		return result

	def is_clickable(self,loc,timeout=10):
		'''
		元素可点击返回本身，不可点击返回False
		:param loc:
		:param timeout:
		:return:
		'''
		result = WebDriverWait(self.driver,timeout,1).until(EC.element_to_be_clickable(loc))
		return result

	def is_located(self,loc,timeout=10):
		'''
		判断元素优美被定位到，定位到返回元素，没定位到返回False
		:param loc:
		:param timeout:
		:return:
		'''
		result = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(loc))
		return result

	def click_alert(self):
		'''
		操作点击弹窗
		:return:
		'''
		alert = self.driver.switch_to.alert
		time.sleep(2)
		alert.accept()
		time.sleep(2)

	def alert_text(self):
		'''
		返回弹窗的文本内容
		:return:
		'''
		alert = self.driver.switch_to.alert()
		rel = alert.text()
		return rel