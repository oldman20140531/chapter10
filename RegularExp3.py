# -*- coding: utf-8 -*-
import re

# ==========================查找字符串中的英文单词，派出字母和其他字符的组合=============================
string = '''
Welcome to Crossin 编程123教室
Hello Python 2and3 World!
hhhhh23333
'''

result = re.findall(r'\b[A-z]+\b', string)
print('result=', result)

# ==========================筛选出手机号码============================================================
string1 = '''
18081530001
13551920001
17778320001
368754
933
119
32148996666
'''

result1 = re.findall(r'1(\d{10})', string1)     #()表示将匹配结果中()显示出来，在正则中成为分组
print('result1=', result1)

