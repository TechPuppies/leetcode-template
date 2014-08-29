# AC Rate: 42.2%
# SOURCE URL: https://oj.leetcode.com/problems/same-tree/
# 
# 
# Given two binary trees, write a function to check if they are equal or not.
# 
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
# 
# 


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        