# -*- coding: utf-8 -*-

import urllib.request
import json

url = 'https://api.douban.com/v2/movie/top250'
req = urllib.request.urlopen(url)
date = req.read()
date_dict = json.loads(date)
print(type(date_dict))
print(date_dict.keys())
print(date_dict['subjects'])
