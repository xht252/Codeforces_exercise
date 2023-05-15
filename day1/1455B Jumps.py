#-*- coding = utf-8 -*-
#@Time : 2023/5/15 21:50
#@Author : xht
#@File : 1455B Jumps.py
#@Software: PyCharm

import math

for _ in range(int(input())):
    x = int(input())
    res = 0
    while x > 0:
        x -= res
        res += 1
    print(res + (x == -1) - 1)
