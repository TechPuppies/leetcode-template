# coding=utf-8
# AC Rate: 26.8%
# SOURCE URL: https://oj.leetcode.com/problems/partition-list/
# 
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# 
# 
# You should preserve the original relative order of the nodes in each of the two partitions.
# 
# 
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
# 
# 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        