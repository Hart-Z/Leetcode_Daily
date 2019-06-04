#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.match("^"+p+"$",s))

