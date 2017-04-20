#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
dict
An online terminal translator
----------------------------------------------------------------------------------

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

	This dictionary is implemented with Youdao Fanyi API, which provides
	translation between Chinese and English.

	The 'key' and 'keyfrom' are needed, you could change these to your 
	own one.
	
	links:	http://fanyi.youdao.com/openapi, http://fanyi.youdao.com
	"""

	def __init__(self, content):
		"""
		Init variables
		----------------------------------------------------------------------------------
		key:        Application ID get from Youdao Fanyi.
		keyfrom:    Secret key get from Youdao Fanyi.

		q:          The content to translate.
		"""

		key = '1698239486'
		keyfrom = 'ren-youdao-dict'

		self.q = " ".join(content)

		self.url = 'http://fanyi.youdao.com/openapi.do' + '?keyfrom=' + keyfrom + '&key=' + key + '&type=data&doctype=json&version=1.1' + '&q=' + urllib.quote(self.q)
 
	def translate(self):
		"""
		Connect to the API and get translated content.
		"""
		
		print("-------------------------------------------------")
		print("有道翻译-fanyi.youdao.com")
		print("-------------------------------------------------")

		if not self.q.strip():
			print("WARNING: nothing to translate.\n")
			exit(1)

		try:
			response = urllib.urlopen(self.url)
			result = eval(response.read().decode('utf-8'))

			if result['errorCode']:
				print("Error %d." % result['errorCode'])
				exit(1)

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

if __name__ == '__main__':
	dict = Dict(sys.argv[1:])
	dict.translate()
