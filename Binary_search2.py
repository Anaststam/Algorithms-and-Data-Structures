"""
# Created by Anastasia on 5/8/20
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) -1

        while left <= right:
                pivot = left + (right - left) // 2
                if target == nums [pivot]:
                    return pivot
                if target < nums[pivot]:
                    right = pivot -1
                else:
                    left = pivot+1
        return -1


solution = Solution()
target_index = solution.search([0,2,3,4,5], 4)
if target_index==-1:
    print("the element doesnt exist in the list")
else:
    print("the index of the target is", target_index)