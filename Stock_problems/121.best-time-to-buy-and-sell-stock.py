#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float("inf")
        res = 0
        for num in prices:
            curr_min = min(num,curr_min)
            res = max(res,num-curr_min)
        return res