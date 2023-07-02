#-*- coding = utf-8 -*-
#@Time : 2023/6/23 16:51
#@Author : xht
#@File : 584A Olesya and Rodion.py
#@Software: PyCharm

n , t = map(int , input().split())
if t == 10 and n != 1:
    print('1' * (n - 1) + '0')
elif t == 10 and n == 1:
    print('-1')
else:
    print(str(t) * n)