# AC Rate: 26.4%
# SOURCE URL: https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 
# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# 


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        