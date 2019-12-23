# 997. Find the Town Judge
# Link: https://leetcode.com/problems/find-the-town-judge/

from typing import List


class Solution:
    @staticmethod
    def findJudge(N: int, trust: List[List[int]]) -> int:
        if len(trust) != 0:
            trust_given = [0]*N
            trust_received = [0]*N
            for x, y in trust:
                trust_given[x-1] += 1
                trust_received[y-1] += 1
            for i in range(0, N):
                if trust_given[i] == 0 and trust_received[i] == N-1:
                    return i+1
            return -1
        else:
            return 1


print(Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
