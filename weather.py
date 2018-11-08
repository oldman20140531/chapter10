# -*- coding:utf-8 -*-
import requests

city = input('请输入城市名：')
url = 'http://wthrcdn.etouch.cn/weather_mini?city='+city
print(url)
r = requests.get(url).json()['data']['forecast'][0]
print(city+'今日'+r['date'][-3:]+','+'最高温度'+r['high'][2:]+','+'最低温度'+r['low'][2:]+','+r['type'])