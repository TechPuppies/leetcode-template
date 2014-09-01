# coding=utf-8
# AC Rate: 25.9%
# SOURCE URL: https://oj.leetcode.com/problems/palindrome-partitioning/
# 
# 
# Given a string s, partition s such that every substring of the partition is a palindrome.
# 
# 
# Return all possible palindrome partitioning of s.
# 
# 
# For example, given s = "aab",
# 
# Return
# 
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]
# 
# 
# 


class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        