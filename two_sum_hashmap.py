class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        dict1 = {}
        for i in range(len(nums)):
            compl = target - nums[i]
            if dict1.get(nums[i]) is not None and compl == nums[i]:
                indices.append(dict1[nums[i]])
                indices.append(i)
                break
            else:
                dict1.update({nums[i]: i})

                compl = target - nums[i]
                if dict1.get(compl) is not None and compl != nums[i]:
                    indices.append(dict1[compl])
                    indices.append(i)
                    break

        return indices