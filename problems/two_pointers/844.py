# 844. Backspace String Compare
# Link: https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def step(s, i):
            count = 0
            while True:
                i += 1
                if i >= len(s):
                    return i
                if s[i] is '#':
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    break
            return i

        revS = S[::-1]
        revT = T[::-1]
        iS = iT = 0

        if revS[iS] == "#":
            iS = step(revS, -1)
            if revT[iT] == "#":
                iT = step(revT, -1)
            if iS >= len(revS) and iT >= len(revT):
                return True

        while iS < len(revS) and iT < len(revT) and revS[iS] == revT[iT]:
            iS = step(revS, iS)
            iT = step(revT, iT)
            if iS >= len(revS) and iT >= len(revT):
                return True
        return False
