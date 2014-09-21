# coding=utf-8
# AC Rate: 18.1%
# https://oj.leetcode.com/problems/minimum-window-substring/

# Given a string S and a string T, find the minimum window in S which will
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
# Note:
# If there is no such window in S that covers all characters in T, return the
# If there are multiple such windows, you are guaranteed that there will always

class Solution:
    # @return a string
    def minWindow(self, S, T):
        