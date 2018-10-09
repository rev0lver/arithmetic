# -*- coding:utf-8 -*-

def fabonacci(num):
    assert num > 0
    if num == 1:
        return 1
    a = 0
    b = 1
    while num > 1:
        a,b = b,a+b
        num -= 1
    return b


result = fabonacci(7)

print result
