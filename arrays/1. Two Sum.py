from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    break
            if nums[i] + nums[j] == target:
                break

        return res


nums = [2,5,5,11]
target = 10
solution = Solution()
print(solution.twoSum(nums, target))

# [5,1,3] [0,2] target 8
