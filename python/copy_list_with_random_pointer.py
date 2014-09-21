# coding=utf-8
# AC Rate: 23.3%
# https://oj.leetcode.com/problems/copy-list-with-random-pointer/

# A linked list is given such that each node contains an additional random
# Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        