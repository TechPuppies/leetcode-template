# coding=utf-8
# AC Rate: 32.3%
# https://oj.leetcode.com/problems/symmetric-tree/

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# For example, this binary tree is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized
# OJ's Binary Tree Serialization:
# The serialization of a binary tree follows a level order traversal, where '#'
# Here's an example:
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        