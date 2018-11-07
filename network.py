# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse

word = urllib.parse.quote(input('search:\n'))
req = urllib.request.urlopen('http://www.baidu.com/s?wd=%s' % word)
date = req.read().decode('utf8')
with open('baidu.html', 'w', encoding='utf8') as f:
    f.write(date)
