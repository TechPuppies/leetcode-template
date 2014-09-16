# coding=utf-8
# AC Rate: 32.1%
# SOURCE URL: https://oj.leetcode.com/problems/gray-code/
#
# The gray code is a binary numeral system where two successive values differ i
# n only one bit.
# Given a non-negative integer n representing the total number of bits in the c
# ode, print the sequence of gray code. A gray code sequence must begin with 0.
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# Note:
# For a given n, a gray code sequence is not uniquely defined.
#
# For example, [0,2,3,1] is also a valid gray code sequence according to the ab
# ove definition.
# For now, the judge is able to judge based on one instance of gray code sequen
# ce. Sorry about that.
#


class Solution:
    # @return a list of integers
    def grayCode(self, n):
        