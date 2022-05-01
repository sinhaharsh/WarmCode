"""
LeetCode #1035 : Uncrossed Lines
[https://leetcode.com/problems/uncrossed-lines/]
Date: May 1 2022
Notes:
    Used Dynamic Programming : Tabulation
    Watched solution. Retry
"""
from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums2)
        n = len(nums1)
        table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        # for k in table:
        #     print(k)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])

        # for k in table:
        #     print(k)
        return table[i][j]