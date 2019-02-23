#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (45.76%)
# Total Accepted:    320.4K
# Total Submissions: 700.1K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#
from heapq import *
class Solution:
    def findKthLargest1(self, nums: 'List[int]', k: 'int') -> 'int':
        Q = []
        for ele in nums:
            heappush(Q,-ele)
        
        for i in range(k-1):
            heappop(Q)
        return - heappop(Q)

    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        
