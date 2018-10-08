# -*- coding:utf-8 -*-

'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

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




