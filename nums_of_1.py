# -*- coding:utf-8 -*-

def num_of_one(n):
    if n < 0:
        s = bin(n & 0xffffffff)
    else:
        s = bin(n)
    return s.count('1')