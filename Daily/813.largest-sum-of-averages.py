#
# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        memo = {}
        def helper(n,k):
            if (n,k) in memo:
                return memo[n,k]
            if n<k:
                return 0
            if k==1:
                memo[n,k] = sum(A[:n])/n
                return memo[n,k]
            curr , memo[n,k] = 0 , 0
            for i in range(n-1,0,-1):
                curr+=A[i]
                memo[n,k] = max(memo[n,k], helper(i,k-1) + curr/(n-i))
            return memo[n,k]
        
        return helper(len(A),K)
