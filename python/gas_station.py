# coding=utf-8
# AC Rate: 25.8%
# SOURCE URL: https://oj.leetcode.com/problems/gas-station/
#
#
# There are N gas stations along a circular route, where the amount of gas at s
# tation i is gas[i].
#
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to trav
# el from station i to its next station (i+1). You begin the journey with an em
# pty tank at one of the gas stations.
#
#
# Return the starting gas station's index if you can travel around the circuit
# once, otherwise return -1.
#
#
# Note:
# The solution is guaranteed to be unique.
#
#


class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        