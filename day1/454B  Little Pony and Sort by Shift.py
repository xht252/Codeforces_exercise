#-*- coding = utf-8 -*-
#@Time : 2023/5/15 20:28
#@Author : xht
#@File : 454B  Little Pony and Sort by Shift.py
#@Software: PyCharm
import copy

n = int(input())
l = list(map(int , input().split()))
l1 = sorted(l)
i = 1
while i < n and l[i] >= l[i - 1]:
    i += 1
print(n - i if l1 == l[i:] + l[:i] else -1)