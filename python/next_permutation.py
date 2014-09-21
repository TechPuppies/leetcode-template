# coding=utf-8
# AC Rate: 25.4%
# https://oj.leetcode.com/problems/next-permutation/

# Implement next permutation, which rearranges numbers into the lexicographically
# If such arrangement is not possible, it must rearrange it as the lowest
# The replacement must be in-place, do not allocate extra memory.
# Here are some examples. Inputs are in the left-hand column and its
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        