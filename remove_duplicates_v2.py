"""
# Created by anastasia on 2/8/20
"""

from typing import List

class Solution:

    def remove_duplicates(self, nums: List[int]) -> int :

        i = 0
        while i <= len(nums) -1:
            if i+1 <= len(nums) -1 and nums[i]==nums[i+1]:
                del nums[i+1]
            i=i+1
        return len(nums), nums


solution = Solution()
new_length, nums= solution.remove_duplicates(nums = [])
print("the new length is:", new_length)
print(nums)
