class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}
        for i in range(len(nums)):
            if (target - nums[i]) in prevNums:
                return [prevNums[target - nums[i]], i]
            else:
                prevNums[nums[i]] = i