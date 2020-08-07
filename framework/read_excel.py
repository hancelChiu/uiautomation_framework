# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/8/6

from xlrd import open_workbook
import os,sys
import getpathInfo
from framework.logger import Logger

pro_dir = getpathInfo.get_path()
logger = Logger(logger="ReadExcel").get_logger()


class ReadExcel():
	def get_xls(self, xls_name, sheet_name):
		cls = []

		# 获取用例文件路径
		excel_path = os.path.join(pro_dir+ '/data/', xls_name)
		try:
			file = open_workbook(excel_path)
			sheet = file.sheet_by_name(sheet_name)
			logger.info("打开的用例数据文件为{}".format(excel_path))
			nrows = sheet.nrows
			for i in range(nrows):
				cls.append(sheet.row_values(i))
			return cls
		except Exception as e:
			logger.error("找不到用例文件 {}".format(e))


if __name__ == "__main__":
	print(ReadExcel().get_xls('data.xlsx', 'Sheet1'))