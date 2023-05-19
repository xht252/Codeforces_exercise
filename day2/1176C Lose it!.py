#-*- coding = utf-8 -*-
#@Time : 2023/5/17 15:32
#@Author : xht
#@File : 1176C Lose it!.py
#@Software: PyCharm

t = int(input())
l = list(map(int , input().split()))
cnt , w = [0] * 7 , [4,8,15,16,23,42]
cnt[0] = t
for i in l:
    x = w.index(i)
    cnt[x + 1] += cnt[x + 1] < cnt[x]
print(t - cnt[6] * 6)