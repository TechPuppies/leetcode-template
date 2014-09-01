# coding=utf-8
# AC Rate: 28.1%
# SOURCE URL: https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/
# 
# 
# Given a binary tree, flatten it to a linked list in-place.
# 
# 
# For example,
# Given
# 
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# 
# 
# 
# The flattened tree should look like:
# 
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# 
# click to show hints.
# Hints:
# If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
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
    # @return nothing, do it in place
    def flatten(self, root):
        