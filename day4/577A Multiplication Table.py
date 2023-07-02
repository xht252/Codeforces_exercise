#-*- coding = utf-8 -*-
#@Time : 2023/6/23 17:36
#@Author : xht
#@File : 577A Multiplication Table.py
#@Software: PyCharm
n , x = map(int , input().split())
print(sum((x % i == 0 and x / i <= n) for i in range(1 , n + 1)))