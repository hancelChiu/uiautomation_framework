# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/8/5

import os
import configparser
import codecs
import getpathInfo

pro_dir = getpathInfo.get_path()
config_path = os.path.join(pro_dir + '/config/config.ini')


class ReadConfig():

	def __init__(self):
		with open(config_path, 'r') as f:
			data = f.read()

			# 移除BOM
			if data[:3] == codecs.BOM_UTF8:
				data = data[3:]
				file = codecs.open(config_path, 'w')
				file.write(data)
				file.close()
		self.cf = configparser.ConfigParser()
		self.cf.read(config_path, encoding='utf-8')


	def get_email(self,name):
		value = self.cf.get("EMAIL", name)
		return value

if __name__ == "__main__":
	print(ReadConfig().get_email('sender'))
