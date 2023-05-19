#-*- coding = utf-8 -*-
#@Time : 2023/5/19 11:13
#@Author : xht
#@File : 520B Two Buttons.py
#@Software: PyCharm

n , m = map(int , input().split());q = 0
while n != m:
    m = [m // 2 , m + 1][m & 1 or m < n];q += 1
print(q)