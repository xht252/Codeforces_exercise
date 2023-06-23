#-*- coding = utf-8 -*-
#@Time : 2023/6/20 13:23
#@Author : xht
#@File : 327A Flipping Game.py
#@Software: PyCharm

n = int(input())
l = list(map(int , input().split()))
print(max(sum(l) + j - i - 2 * sum(l[i:j]) for i in range(n) for j in range(i + 1 , n + 1)))