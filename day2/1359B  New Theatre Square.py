#-*- coding = utf-8 -*-
#@Time : 2023/5/16 16:23
#@Author : xht
#@File : 1359B  New Theatre Square.py
#@Software: PyCharm

for _ in range(int(input())):
    n , m , x , y = map(int , input().split())
    g = []
    for i in range(n):
        s = input()
        s.replace('*' , '')
        g.append(s)

    res = 0
    for i in range(n):
        a , b = 0 , 0
        w = len(g[i])
        for j in g[i]:
            if j == '.':
                a += x
        j = 0
        while j < w:
            if g[i][j] == '.':
                if j + 1 < w and g[i][j + 1] == '.':
                    b += y
                    j += 1
                else:
                    b += x
            j += 1
        res += min(a , b)

    print(res)