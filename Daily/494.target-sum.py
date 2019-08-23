#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from collections import Counter
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = Counter([0])

        for num in nums:
            tmp = Counter()
            for ele in memo:
                tmp[ele+num] += memo[ele]
                tmp[ele-num] += memo[ele]
            memo = tmp

        return memo[S]

