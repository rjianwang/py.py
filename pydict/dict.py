#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
	dict
	An online terminal dictionary
	-----------------------------------------------------------------
	
	Author:		rjianwang
	Email:		rjianwang@foxmail.com
	Date:		2017-04-19
	License:	The MIT License, please visit https://mitlicense.org/
				for more details.
"""

import sys
import httplib
import md5
import urllib
import random

class Dict:
	"""
	An online terminal dictionary.

	This dictionary is implemented with Baidu Fanyi API, which provides
	translation of dozens of languages.

	The 'appid' and 'secretkey' are needed, you could change these to 
	your own one.
	
	links:	http://api.fanyi.baidu.com/api/trans/product/index
			http://fanyi.baidu.com
	"""

	def __init__(self, content, fromLang = 'en', toLang = 'zh'):
		"""
		Init variables
		------------------------------------------------------------------
		appid:		Application ID get from Baidu Fanyi.
		secretKey:	Secret key get from Baidu Fanyi.

		fromLang:	The source language with a default value 'en'.
		toLang:		The destinatin language with a default value 'zh'.

		q:			The content to translate.

		salt:		A random number
		sign:		Signature, create with appid, q, salt, and MD5 code of
					secretKey.
		"""

		appid = '20170419000045161'
		secretKey = 'PuP92ns9ufmGnO2_s8Ef'

		self.httpClient = None
		self.url = '/api/trans/vip/translate'
		self.q = " ".join(content)
		self.fromLang = 'en'
		self.toLang = 'zh'
		self.salt = random.randint(32768, 65536)

		self.sign = appid + str(self.q) + str(self.salt) + secretKey
		m1 = md5.new()
		m1.update(self.sign)
		self.sign = m1.hexdigest()
		self.url = self.url + '?appid=' + appid + '&q=' + urllib.quote(self.q) + '&from=' + self.fromLang + '&to=' + self.toLang + '&salt=' + str(self.salt) + '&sign=' + self.sign
 
	def translate(self):
		"""
		Connect to the API and get translated content.
		"""

		if not self.q.strip():
			print("WARNING: nothing to translate.\n")
			exit(1)

		try:
			httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
			httpClient.request('GET', self.url)
		 
			#response是HTTPResponse对象
			response = httpClient.getresponse()
			result = eval(response.read().decode('utf-8'))

			for content in result["trans_result"]:
				print("%s" % content["src"])
				print("%s\n" % urllib.unquote(content["dst"]).decode('unicode-escape'))

		except Exception, e:
			print e
		finally:
			if httpClient:
				httpClient.close()

if __name__ == '__main__':
	dict = Dict(sys.argv[1:])
	dict.translate()