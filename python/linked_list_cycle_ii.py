# AC Rate: 30.9%
# SOURCE URL: https://oj.leetcode.com/problems/linked-list-cycle-ii/
# 
# 
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# 
# 
# Follow up:
# Can you solve it without using extra space?
# 
# 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        