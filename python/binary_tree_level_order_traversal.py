# coding=utf-8
# AC Rate: 30.9%
# SOURCE URL: https://oj.leetcode.com/problems/binary-tree-level-order-traversal/
# 
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# 
# For example:
# Given binary tree {3,9,20,#,#,15,7},
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# 
# 
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
# OJ's Binary Tree Serialization:
# 
# The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.
# 
# 
# Here's an example:
# 
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# 
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}". 
# 
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
    # @return a list of lists of integers
    def levelOrder(self, root):
        