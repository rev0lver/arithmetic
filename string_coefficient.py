# -*- coding:utf-8 -*-

# tencent

class Solution(object):
    def __init__(self,a,b,k):
        self.a = a
        self.b = b
        self.k = k
    def get_coefficient(self):
        cnt = 0
        str_set = set()

        for i in range(len(self.a)-self.k+1):
            str_set.add(self.a[i:i+self.k])
        for sub_str in str_set:
            cnt += self.b.count(sub_str)
        print cnt

s = Solution('abab','abababc',2)
r = s.get_coefficient()

class TriTuple(object):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def solve(self):
        cnt = 0
        for i in range(1,self.a+1):
            for j in range(1,self.b+1):
                min_c = abs(i-j)+1
                max_c = min(i+j-1,self.c)
                cnt += max_c - min_c + 1
        return cnt%1000000007

x = TriTuple(2,3,3)
print x.solve()

