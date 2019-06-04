#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (31.22%)
# Total Accepted:    92.2K
# Total Submissions: 295.2K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#
from collections import Counter

class Solution:
    def majorityElement1(self, nums: 'List[int]') -> 'List[int]':
        count = Counter(nums)
        return [i for i in count if count[i]>len(nums)/3]
    

    def majorityElement(self, nums: 'List[int]') -> 'List[int]':
        if not nums:
            return []

        count1 , count2 , candidate1 ,candidate2 = 0, 0, 0, 1

        for i in nums:
            if i == candidate1:
                count1 += 1
            elif i == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 , count1 = i, 1
            elif count2 == 0:
                candidate2 , count2 = i, 1
            else:
                count1, count2 = count1-1 , count2-1
        return [i for i in [candidate1,candidate2] if nums.count(i)>len(nums)//3]
