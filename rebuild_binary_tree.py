# -*- coding:utf-8 -*-


pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def solution(pre,tin):
    if not pre:
        return None
    root = Node(pre[0])
    index = tin.index(pre[0])
    root.left = solution(pre[1:index+1],tin[:index])
    root.right = solution(pre[index+1:],tin[index+1:])
    return root

node = solution(pre,tin)




