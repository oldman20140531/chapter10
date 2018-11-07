# -*- coding: utf-8 -*-
import urllib.request

url = 'http://m.weather.com.cn/data3/city.xml'
req = urllib.request.urlopen(url)
data = req.read().decode('utf8')
print(data)
data_list = data.split(',')
for d in data_list:
    print(d)

