#-*- coding = utf-8 -*-
#@Time : 2023/6/23 17:07
#@Author : xht
#@File : 476A Dreamoon and Stairs.py
#@Software: PyCharm
import math
n , m = map(int , input().split())
lb = n - n // 2
res = lb + (-lb) % m
if res > n:
    res = -1

print(int(res))