#-*- coding = utf-8 -*-
#@Time : 2023/5/28 16:06
#@Author : xht
#@File : 1837C Best Binary.py
#@Software: PyCharm

for _ in range(int(input())):
    s = list(input())
    n , ch = len(s) , '0'

    for i in range(n):
        if s[i] == '?':
            s[i] = ch
        else:
            ch = s[i]

    print("".join(s))