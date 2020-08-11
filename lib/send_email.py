#!/usr/bin/env python
#-*- coding:utf-8 -*-

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import sys
sys.path.append("../")
from lib.get_data import get_data
import smtplib

def send_email():
	#获取收件人、发件人、密码、标题、服务器、文件路径信息
	toAddr = get_data('mail',"to_addr")
	fromAddr = get_data('mail',"from_addr")
	password = get_data('mail',"from_password")
	title = get_data('mail',"title")
	smtpserver = get_data('mail',"server")
	html_dir = get_data('mail','html_dir')

	#读取HTML文件内容
	f = open(html_dir,"rb")
	mail_boby = f.read()
	f.close()


	#邮件内容格式编码
	message = MIMEMultipart()
	txt = MIMEText(mail_boby,'html','utf-8')
	message.attach(txt)
	message['From'] = (u'tester<%s>'%fromAddr)
	message['To'] = (u'other<%s>'%toAddr)
	message['Subject'] = Header(u'自动化测试<%s>'%title,'utf-8')

	#添加HTML附件
	part = MIMEApplication(open(html_dir,'rb').read())
	part.add_header('Content-Disposition','attachment',filename="report.html")
	message.attach(part)


	try:
		server = smtplib.SMTP()
		server.connect(smtpserver,25)
		#server.set_debuglevel(1)
		server.login(fromAddr,password)
		server.sendmail(fromAddr,toAddr,message.as_string())
		print("发送邮件成功")
		server.quit()
	except smtplib.SMTPException:
		print("发送邮件失败")

if __name__ == '__main__':
	send_email()