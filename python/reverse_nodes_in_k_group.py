# AC Rate: 24.8%
# SOURCE URL: https://oj.leetcode.com/problems/reverse-nodes-in-k-group/
# 
# 
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# 
# 
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# You may not alter the values in the nodes, only nodes itself may be changed.
# Only constant memory is allowed.
# 
# For example,
# Given this linked list: 1->2->3->4->5
# 
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        