# -*- coding: utf-8 -*-
import requests

url = 'https://api.douban.com/v2/movie/top250'
req = requests.get(url)
print(req)              # req 返回值表示状态，200为正常
print(type(req.text))   # req.txt类型为str
data = req.json()
print(type(data))       # .json()函数将json返回成字典
print(data['title'])
print(req.status_code)  #  状态码