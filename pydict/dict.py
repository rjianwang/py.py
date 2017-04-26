#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
dict
An online terminal translator
---------------------------------------------------------------------------------------

Author:		rjianwang
Email:		rjianwang@foxmail.com
Date:		2017-04-19

License:	The MIT License, please visit https://mitlicense.org for more details.
"""

import sys
import urllib

class Dict:
	"""
	An online terminal translator.

	This translator is implemented with Youdao Fanyi API, which provides
	translation between Chinese and English.

	The 'key' and 'keyfrom' are needed, you could change these to your 
	own ones.
	
	links:	http://fanyi.youdao.com/openapi, http://fanyi.youdao.com
	"""

	def __init__(self):
		"""
		Init variables
		----------------------------------------------------------------------------------
		key:        Application ID get from Youdao Fanyi.
		keyfrom:    Secret key get from Youdao Fanyi.
		"""

		key = '1698239486'
		keyfrom = 'ren-youdao-dict'

		self.url = 'http://fanyi.youdao.com/openapi.do' + '?keyfrom=' + keyfrom + '&key=' + key + '&type=data&doctype=json&version=1.1'
 
	def translate(self, content):
		"""
		Connect to the API and get translated content.
		"""
		
		print("-------------------------------------------------")
		print("有道翻译-fanyi.youdao.com")
		print("-------------------------------------------------")
		
		self.q = " ".join(content)
		self.url = self.url + '&q=' + urllib.quote(self.q)

		if not self.q.strip():
			print("WARNING: nothing to translate.\n")
			exit(1)

		try:
			response = urllib.urlopen(self.url)
			result = eval(response.read().decode('utf-8'))

			# error
			if self.error(result):
				exit(1)

			# show translation
			print("%s\n" % result['query'])
			if result.has_key('translation'):
				for item in result['translation']:
					print(urllib.unquote(item))
			if result.has_key('web'):
				for items in result['web']:
					item = ", ".join(items['value'])
					print(urllib.unquote(item))

			print("")
		except Exception, e:
			print e
	
	def error(self, result):
		"""
		Error check.

		0 means there is nothing wrong. The others means translation meet 
		some troubles.
		"""
		if result['errorCode'] == 0:
			return 0
		elif result['errorCode'] == 20:
			print("ERROR: the query content is too long to translate.")
			return 1
		elif result['errorCode'] == 30:
			print("ERROR: cannot translate.")
			return 1
		elif result['errorCode'] == 40:
			print("ERROR: unsuported language.")
			return 1
		elif result['errorCode'] == 50:
			print("ERROR: invalid key.")
			return 1
		elif result['errorCode'] == 60:
			print("ERROR: the result content is empty.")
			return 1

if __name__ == '__main__':
	dict = Dict()
	dict.translate(sys.argv[1:])
