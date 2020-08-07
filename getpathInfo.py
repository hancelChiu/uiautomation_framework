# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/6/19

import os

def get_path():
	# os.path.split()：按照路径将文件名和路径分割开
	path = os.path.split(os.path.abspath(__file__))[0]
	return path

if __name__ == '__main__':
	print('当前路径：', get_path())