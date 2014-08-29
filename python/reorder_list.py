# AC Rate: 20.3%
# SOURCE URL: https://oj.leetcode.com/problems/reorder-list/
# 
# 
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# You must do this in-place without altering the nodes' values.
# 
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
# 
# 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        