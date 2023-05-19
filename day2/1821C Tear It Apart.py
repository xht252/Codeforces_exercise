#-*- coding = utf-8 -*-
#@Time : 2023/5/17 17:08
#@Author : xht
#@File : 1821C Tear It Apart.py
#@Software: PyCharm

for _ in range(int(input())):
    s = input()
    st = set(s)

    minv = 0x3f3f3f3f
    for c in st:
        minv = min(minv, max(map(len, s.split(c))))

    print(0 if not minv else len(bin(minv)) - 2)
