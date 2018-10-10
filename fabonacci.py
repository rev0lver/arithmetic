# -*- coding:utf-8 -*-

def fabonacci(num):
    assert num > 0
    n, a, b = 0, 0, 1
    while n < num-1:
        a, b = b, a + b
        n += 1
    return b

def fab_with_list(num):
    assert num > 0
    a = 0
    b = 1
    fab_list = [1]
    for i in range(num - 1):
        a, b = b, a + b
        fab_list.append(b)
    return fab_list

def fib_generator(num):
    n,a,b = 0,0,1
    while n < num:
        yield b
        a,b = b,a+b
        n += 1

result = fabonacci(3)
l = fab_with_list(5)
l1 = fab_with_list(1)
l2 = fab_with_list(2)
g = fib_generator(5)
for i in g:
    print i
