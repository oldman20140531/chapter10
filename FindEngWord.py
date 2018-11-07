# -*- coding: utf-8 -*-
import re

with open('from.txt', encoding='utf8') as f:
    word = re.findall(r'\b[A-z]+\b', f.read())      # 提取文件，查找英文单词
word.sort()                                         # 排序
with open('to.txt', 'w', encoding='utf8') as f:
    f.write('\n'.join(i for i in word))             # 将word列表重组为一个字符串并加入换行符后写入新文件

