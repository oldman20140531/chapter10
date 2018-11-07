# -*- coding: utf-8 -*-
import requests

url = 'https://www.google.com'
req_header = {
    'User-Agent': 'Chrome',  # 定义headers的值，字典格式
    # 'Host': 'xueqiu.com',
    # 'Referer': 'https://xueqiu.com',
}
try:
    req = requests.get(url, headers=req_header, timeout=1)
    print(req.text)
except:
    print('timeout')
