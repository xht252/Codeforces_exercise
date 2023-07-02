#-*- coding = utf-8 -*-
#@Time : 2023/6/23 17:25
#@Author : xht
#@File : 742A Arpa’s hard exam and Mehrdad’s naive cheat.py
#@Software: PyCharm
n = int(input())
res = [6 , 8 , 4 , 2]
print(res[n % 4] if n != 0 else 1)