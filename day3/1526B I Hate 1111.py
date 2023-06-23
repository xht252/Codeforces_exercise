#-*- coding = utf-8 -*-
#@Time : 2023/5/28 16:26
#@Author : xht
#@File : 1526B I Hate 1111.py
#@Software: PyCharm

for _ in range(int(input())):
    x = int(input())
    print('YES' if x >= 111 * (x % 11) else 'NO')