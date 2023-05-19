#-*- coding = utf-8 -*-
#@Time : 2023/5/18 8:23
#@Author : xht
#@File : 1294C Product of Three Numbers.py
#@Software: PyCharm

import bisect
import math

for _ in range(int(input())):
    n = int(input())
    # n = _ + 1
    t = n
    d = {}
    check = 0
    a , b = -1 , -1
    for i in range(2 , int(math.sqrt(n) + 1)):
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        if cnt != 0:
            if a == -1 and cnt >= 1:
                a = i
                cnt -= 1
            if b == -1 and cnt >= 1 and a != i:
                b = i
                cnt -= 1
            elif b == -1 and cnt >= 2:
                b = i * i
                cnt -= 2
            d[i] = cnt

    if n > 1:
        d[n] = 1

    n = t
    c = 1
    for i , j in d.items():
        c *= i ** j

    if a >= 2 and b >= 2 and c != a and c != b and c >= 2 and a * b * c == n:
        print('YES')
        print(a , b , c)
    else:
        print('NO')