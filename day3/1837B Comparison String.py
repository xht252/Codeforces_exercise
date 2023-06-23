#-*- coding = utf-8 -*-
#@Time : 2023/5/28 15:35
#@Author : xht
#@File : 1837B Comparison String.py
#@Software: PyCharm

for _ in range(int(input())):
    n = int(input())
    s = input()

    res , cur = 1 , 1
    for i in range(1 , n):
        if s[i] != s[i - 1]:
            cur = 1
        else:
            cur += 1
        res = max(res , cur)

    print(res + 1)