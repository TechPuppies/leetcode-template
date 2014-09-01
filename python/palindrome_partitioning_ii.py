# coding=utf-8
# AC Rate: 18.0%
# SOURCE URL: https://oj.leetcode.com/problems/palindrome-partitioning-ii/
# 
# 
# Given a string s, partition s such that every substring of the partition is a palindrome.
# 
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# 
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
# 
# 


class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        