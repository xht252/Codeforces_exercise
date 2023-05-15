#-*- coding = utf-8 -*-
#@Time : 2023/5/15 16:17
#@Author : xht
#@File : 1328C Ternary XOR.py
#@Software: PyCharm

# a b c

# 0 0 0
# 0 1 1
# 0 2 2

# 1 0 1
# 1 1 2
# 1 2 0

# 2 0 2
# 2 1 0
# 2 2 1

for _ in range(int(input())):
    n = int(input())
    s = input()
    a , b = "" , ""
    is_first = True
    for i in range(n):
        if s[i] == '0':
            a += '0'
            b += '0'
        elif s[i] == '1':
            if not is_first:
                a += '0'
                b += '1'
            else:
                is_first = False
                a += '1'
                b += '0'
        else:
            if is_first:
                a += '1'
                b += '1'
            else:
                a += '0'
                b += '2'

    print(a)
    print(b)