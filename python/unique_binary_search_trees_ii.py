# coding=utf-8
# AC Rate: 27.3%
# SOURCE URL: https://oj.leetcode.com/problems/unique-binary-search-trees-ii/
# 
# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
# 
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
# 
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
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
    # @return a list of tree node
    def generateTrees(self, n):
        