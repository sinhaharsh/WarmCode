"""
LeetCode #1035 : Uncrossed Lines
[https://leetcode.com/problems/backspace-string-compare/]
Date: May 1 2022
Notes:
    Used iterative procedure, easy
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstr = [""] * len(s)
        j = 0
        for i in range(len(s)):
            if s[i] != '#':
                sstr[j] = s[i]
                j += 1
            else:
                j -= 1
                sstr[j] = ""
                if j < 0:
                    j = 0

        tstr = [""] * len(t)
        j = 0
        for i in range(len(t)):
            # print(tstr, j)
            if t[i] != '#':
                tstr[j] = t[i]
                j += 1
            else:
                # print("Deleting..", j)
                j -= 1
                tstr[j] = ""
                if j < 0:
                    j = 0
        w = "".join(sstr)
        v = "".join(tstr)
        # print(w, v)
        return w == v


