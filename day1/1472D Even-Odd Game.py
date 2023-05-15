#-*- coding = utf-8 -*-
#@Time : 2023/5/15 19:16
#@Author : xht
#@File : 1472D Even-Odd Game.py
#@Software: PyCharm

for _ in range(int(input())):
    n , k = map(int , input().split())
    if n & 1:
        print(1 , n // 2 , n // 2)
    else:
        if n % 4 == 0:
            print(n // 2 , n // 4 , n // 4)
        else:
            print(n // 2 - 1 , n // 2 - 1 , 2)