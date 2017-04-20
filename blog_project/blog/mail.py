# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
import logging

def sendmail(sender, receiver_list, sub, content):
	
	msg = MIMEText(content, _subtype = 'plain', _charset = 'utf-8')
	msg['Subject'] = sub
	msg['From'] = sender
	msg['To'] = ";".join(receiver_list)

	try:
		server = smtplib.SMTP()
		server.connect('smtp.qq.com')
		server.login(sender, "WANGYUREN_880423")
		server.sendmail(sender, receiver_list, msg.as_string())
		server.close()
		return True
	except Exception as e:
		print(e)
		return False
