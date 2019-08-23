#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        S = []
        ops = {
            "+": lambda x1, x2: x1+x2,
            "-": lambda x1, x2: x1-x2,
            "*": lambda x1, x2: x1*x2,
            "/": lambda x1, x2: int(x1/x2)
        }

        for ele in tokens:
            if ele not in ops:
                S.append(int(ele))
            else:
                op2 = S.pop()
                op1 = S.pop()
                S.append(ops[ele](op1,op2))
        
        return S[-1]
            

