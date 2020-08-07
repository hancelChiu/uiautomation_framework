# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/8/6


import logging
import os
import time
import getpathInfo

pro_dir = getpathInfo.get_path()


class Logger():

	def __init__(self, logger):
		'''
		指定保存日志的文件路径，日志级别，以及调用文件
		:param logger:
		'''
		# 创建一个logger
		self.logger = logging.getLogger(logger)
		self.logger.setLevel(logging.DEBUG)

		# 创建一个handler，用于写入日志文件
		now = time.strftime("%Y-%m-%d_%H_%M_%S")
		log_path = pro_dir + '/logs/'
		log_name = log_path + now +'.log'

		file_handle = logging.FileHandler(log_name, encoding="utf-8")
		file_handle.setLevel(logging.INFO)

		# 创建一个handle，用来输出日志到控制台
		control_handle = logging.StreamHandler()
		control_handle.setLevel(logging.INFO)

		# 将输出的handle格式进行转换
		formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
		file_handle.setFormatter(formatter)
		control_handle.setFormatter(formatter)

		# 给logger添加handle
		self.logger.addHandler(file_handle)
		self.logger.addHandler(control_handle)

	def get_logger(self):

		return self.logger
