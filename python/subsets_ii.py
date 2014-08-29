# AC Rate: 26.9%
# SOURCE URL: https://oj.leetcode.com/problems/subsets-ii/
# 
# 
# Given a collection of integers that might contain duplicates, S, return all possible subsets.
# 
# Note:
# 
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# 
# 
# 
# For example,
# If S = [1,2,2], a solution is:
# 
# 
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
# 
# 


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        