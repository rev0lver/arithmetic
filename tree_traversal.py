# -*- coding:utf-8 -*-
'''
     a
     /\
    b  c
   /\  /
  d  e f
'''
class BinaryTreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

n1 = BinaryTreeNode(data="D")
n2 = BinaryTreeNode(data="E")
n3 = BinaryTreeNode(data="F")
n4 = BinaryTreeNode(data="B", left=n1, right=n2)
n5 = BinaryTreeNode(data="C", left=n3, right=None)
root = BinaryTreeNode(data="A", left=n4, right=n5)


class TreeTraversal(object):
    def __init__(self,root):
        self.root =  root
        self.node_list = []
    def pre_order(self,node):
        if not node:
            return
        self.node_list.append(node)
        self.pre_order(node.left)
        self.pre_order(node.right)
        return
    def in_order(self,node):
        if not node:
            return
        self.pre_order(node.left)
        self.node_list.append(node)
        self.pre_order(node.right)
        return

tree_traversal = TreeTraversal(root)
tree_traversal.pre_order(tree_traversal.root)

print [tree.data for tree in tree_traversal.node_list]