# -*- coding:utf-8 -*-
import re

with open('english.txt', encoding='utf8') as f:
    s = f.read()
c = re.compile(r'[A-z\'&-]+')   # i'm,rock&roll,co-op算作一个单词，不知道这么写对不对，我寻思
r = re.findall(c, s)
print('english.txt文件中共有%d个单词' % len(r))
