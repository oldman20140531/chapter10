# -*- coding: utf-8 -*-

import re

string = 'lance 四川123达州 lhi233333'

result = re.findall(r'\d+', string)         #\d表示任意一个数字，+表示重复一次或多次，贪婪匹配（一次匹配尽可能多的字符）
print('result=', result)

result1 = re.findall(r'\d?', '1a23')        #?表示重复零次或一次
print('result1=', result1)

result2 = re.findall(r'\d*', '1a23')        #*表示重复任意次包括零次
print('result2=', result2)

result3 = re.findall(r'.*', string)         #.表示任意一个字符
print('result3=', result3)

result4 = re.findall(r'\d{2}', string)      #{2}表示字符长度为2，{2,6}表示2到6个字符
print('result4=', result4)

result5 = re.findall(r'[0-9]+|[A-z]+', string)      #[A-z]表示匹配从A到z任意一个字符,|表示规则的OR逻辑运算
print('result5=', result5)

result6 = re.findall(r'^l.|.3$', string)            #^表示字符串起始位置，不表示任何字符，$表示字符串结尾
print('result6=', result6)

result7 = re.findall(r'\w+', string)                #\w表示任意文字字符，python3中包括中文
print('result7=', result7)

result8 = re.findall(r'\sl', string)                #\s表示空格或制表符
print('result8=', result8)
# \B非边界，\S非空白符，\W非文字，\D非数字

result9 = re.findall(r'[^0-9\s]+', string)          #[]中的^表示出[]之外的其他字符，注意与[]外的^做区别
print('result9=', result9)