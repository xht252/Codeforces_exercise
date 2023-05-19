#-*- coding = utf-8 -*-
#@Time : 2023/5/16 16:43
#@Author : xht
#@File : 1182A Filling Shapes.py
#@Software: PyCharm

n = int(input())
print(0 if n & 1 else 1 << (n // 2))