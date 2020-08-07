# -*- coding: utf-8 -*-
#_author:"hancel"
#date:2020/8/6

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
from framework.read_config import ReadConfig
from framework.logger import Logger

email_config = ReadConfig()
logger = Logger(logger="SendEmail").get_logger()


class SendEmail():

	def __init__(self):
		self.host = email_config.get_email('mail_host')
		self.user = email_config.get_email('mail_user')
		self.password = email_config.get_email('mail_pass')
		self.port = email_config.get_email('mail_port')
		self.sender = email_config.get_email('sender')
		self.receiver = email_config.get_email('receiver')
		self.title = email_config.get_email('subject')
		self.content = email_config.get_email('content')
		self.receiver = email_config.get_email('receiver')
		# 定义邮件主题
	def send_email(self, report_name):

		receiver = []
		for i in str(self.receiver).split(','):
			receiver.append(i)
		date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		subject = self.title +"" + date

		# 创建带附件的实例
		message = MIMEMultipart()
		message['From'] = self.sender
		message['To'] = ';'.join(self.receiver)
		message['Subject'] = Header(subject, 'utf-8')

		# 邮件正文内容
		message.attach(MIMEText(self.content, 'plain', 'utf-8'))
		att = MIMEText(open(report_name, 'rb').read(), 'base64', 'utf-8')
		att["Content-Type"] = 'application/octet-stream'
		att["Content-Disposition"] = 'attachment; filename="report_test.html"'
		message.attach(att)
		try:
			smtp = smtplib.SMTP_SSL()
			smtp.connect(self.host)
			smtp.login(self.user,self.password)
			smtp.sendmail(self.sender, receiver, message.as_string())
			print("邮件发送成功！！！")
			logger.info("邮件发送成功！！！")

			smtp.quit()
		except Exception as e:
			logger.error("邮件发送失败{}".format(e))
			print("失败")
if __name__ == "__main__":
	email = SendEmail()
	email.send_email(r"F:\Python\uiautomation_framework\test_report\2020-08-06_16_28_39_result.html")
