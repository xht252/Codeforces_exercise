#-*- coding = utf-8 -*-
#@Time : 2023/5/16 15:59
#@Author : xht
#@File : 996A Hit the Lottery.py
#@Software: PyCharm

mon = [100 , 20 , 10 , 5 , 1]
n = int(input())
res = 0
for i in mon:
    res += int(n // i)
    n %= i
print(res)