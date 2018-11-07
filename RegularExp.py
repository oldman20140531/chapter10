# -*- coding: utf-8 -*-

import re

string1 = 'Hi I am Shirley Hilton. I am his wife.'
string2 = 'abcdefghjkhmn'
pattern1 = r'hi'    # 定义匹配规则pattern1
# pattern = re.compile(r'hi')               #使用re.compile编译一个正则表达式，返回一个规则对象
# result = pattern.findall(string1)         #用编译后的规则对象的findall方法，可以提高程序运行效率

result1 = re.findall(pattern1, string1)     #findall方法查找匹配的字符串，返回列表,没有匹配返回空列表
print(result1)

result2 = re.search(pattern1, string1)      #search方法检索字符串，返回一个符合规则的匹配对象。没有则返回None
print(result2)
print(result2.group())                      #group方法调用search返回值的内容

result3 = re.match(r'[Hh]i', string1)       #match从开始处检索字符串，返回一个符合规则的匹配对象。没有则返回None
print(result3)
print(result3.group())                      #[]表示匹配括号内的任意一个字符

result4 = re.findall(r'\b[hH]i\b', string1)     #\b表示字符串边界,[abc]表示匹配[]中的任何一个字符
print(result4)