#-*- coding = utf-8 -*-
#@Time : 2023/5/15 21:10
#@Author : xht
#@File : 1772D  Absolute Sorting.py
#@Software: PyCharm

for _ in range(int(input())):
    n = int(input())
    l = list(map(int , input().split()))

    x , y , z = 0 , 1e9 , l[0]
    for i in range(1 , n):
        if z < l[i]:
            y = min(y , (z + l[i]) // 2)
        elif z > l[i]:
            x = max(x , (z + l[i] + 1) // 2)
        z = l[i]

    print(-1 if x > y else x)