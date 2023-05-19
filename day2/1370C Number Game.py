#-*- coding = utf-8 -*-
#@Time : 2023/5/19 22:15
#@Author : xht
#@File : 1370C Number Game.py
#@Software: PyCharm

for _ in range(int(input())):
    n = int(input())
    print(('FastestFinger','Ashishgup')[n == 2 or (n & -n < n ) & (n | any(n % i == 0 for i in range(3 , int(n ** .5)+1)))])