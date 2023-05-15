#-*- coding = utf-8 -*-
#@Time : 2023/5/15 20:16
#@Author : xht
#@File : 1514B  AND 0, Sum Big.py
#@Software: PyCharm
mod = 1000000007

for _ in range(int(input())):
    n , k = map(int , input().split())
    print(n ** k % mod)