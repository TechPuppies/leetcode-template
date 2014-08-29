# AC Rate: 20.0%
# SOURCE URL: https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/
# 
# 
# Given a binary tree, find the maximum path sum.
# 
# 
# The path may start and end at any node in the tree.
# 
# 
# For example:
# Given the below binary tree,
# 
#        1
#       / \
#      2   3
# 
# 
# 
# Return 6.
# 
# 


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        