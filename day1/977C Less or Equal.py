#-*- coding = utf-8 -*-
#@Time : 2023/5/15 16:38
#@Author : xht
#@File : 977C Less or Equal.py
#@Software: PyCharm

n , k = map(int , input().split())
l = list(map(int , input().split()))
l.sort()
if k == 0:
    if l[0] != 1:
        print(1)
    else:
        print(-1)
else:
    if k == n:
        print(l[-1])
    else:
        if l[k] - l[k - 1] < 1:
            print(-1)
        else:
            print(l[k - 1])