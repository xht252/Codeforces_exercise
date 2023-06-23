#-*- coding = utf-8 -*-
#@Time : 2023/5/31 16:48
#@Author : xht
#@File : 1515C  Phoenix and Towers.py
#@Software: PyCharm

for _ in range(int(input())):
    n , m , k = map(int , input().split())
    l = list(map(int , input().split()))

    s = sorted(range(n) , key = lambda i : l[i])
    res = [0] * n
    c = 0

    for i in s:
        res[i] = c + 1
        c = (c + 1) % m
    print('YES')
    print(*res)