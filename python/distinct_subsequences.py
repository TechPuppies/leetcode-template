# coding=utf-8
# AC Rate: 24.9%
# https://oj.leetcode.com/problems/distinct-subsequences/

# Given a string S and a string T, count the number of distinct subsequences of T
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing the
# relative positions of the remaining characters. (ie, "ACE" is a subsequence of
# Here is an example:
# S = "rabbbit", T = "rabbit"
# Return 3.

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        