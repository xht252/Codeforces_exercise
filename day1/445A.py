#-*- coding = utf-8 -*-
#@Time : 2023/5/15 18:53
#@Author : xht
#@File : 445A.py
#@Software: PyCharm

n , m = map(int , input().split())
for _ in range(n):
    s = input()
    t = ""
    for i in range(m):
        if s[i] == '-':
            t += '-'
        else:
            if (i + _) & 1:
                t += 'W'
            else:
                t += 'B'
    print(t)