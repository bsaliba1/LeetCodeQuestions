# 136. Single Number
# Link: https://leetcode.com/problems/single-number/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ref = {}
        for i in nums:
            if i not in ref:
                ref[i] = 0
            else:
                ref[i] += 1

        for k, v in ref.items():
            if not v:
                return k

    def singleNum(self, nums: List[int]) -> int:
        sol = 0
        for n in nums:
            sol ^= n

        return sol


print(Solution().singleNum([2, 2, 1]))








