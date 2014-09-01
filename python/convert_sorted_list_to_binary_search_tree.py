# coding=utf-8
# AC Rate: 27.3%
# SOURCE URL: https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# 
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
# 


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        