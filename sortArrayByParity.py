"""
LeetCode #905 : Sort Array by Parity
[https://leetcode.com/problems/sort-array-by-parity/]
Date: May 2 2022
Notes:
    Easy problem, maintain two pointers from beginning and the end, swap elements to get
    the requirements fulfilled.
"""
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        while i < j:
            # print(i, j)
            #i is even, just continue
            if nums[i]%2 == 0:
                i += 1
            #i is odd,
            else:
                #j is even, swap
                if nums[j]%2 == 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    j = j-1
                    i = i+1
                #j is odd
                else:
                    j =j-1
        return nums