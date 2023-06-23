#-*- coding = utf-8 -*-
#@Time : 2023/6/20 13:38
#@Author : xht
#@File : 514A.py
#@Software: PyCharm

l = input()
res = ''
for i in range(len(l)):
    if 9 - int(l[i]) == 0 and i == 0:
        res += '9'
    else:
        res += str(min(9 - int(l[i]) , int(l[i])))
print(int(res))