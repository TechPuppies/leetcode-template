# coding=utf-8
# AC Rate: 26.8%
# https://oj.leetcode.com/problems/triangle/

# Given a triangle, find the minimum path sum from top to bottom. Each step you
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        