#-*- coding = utf-8 -*-
#@Time : 2023/5/31 17:17
#@Author : xht
#@File : 1714E Add Modulo 10.py
#@Software: PyCharm

for _ in range(int(input())):
    n = int(input())
    l = list(map(int , input().split()))
    res = set()

    for i in l:
        while i % 10 and i % 10 != 2:
            i += i % 10
        if i % 10:
            i %= 20

        res.add(i)

    print('YES' if len(res) == 1 else 'NO')