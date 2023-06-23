#-*- coding = utf-8 -*-
#@Time : 2023/5/28 16:18
#@Author : xht
#@File : 1285C Fadi and LCM.py
#@Software: PyCharm

import math

x = int(input())
res , i , = 1 , 1
while i * i <= x:
    if x % i == 0 and math.gcd(x // i , i) == 1:
        res = i
    i += 1
print(res , x // res)