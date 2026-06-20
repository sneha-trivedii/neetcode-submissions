class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
            Use Hash Maps to store frequency of integers and flag as duplicate
            when frequency of any integer becomes 1.
        '''
        freqNums = {}
        for i in range(len(nums)):
            if freqNums.get(nums[i] , 0) == 1:
                return True
            freqNums[nums[i]] = 1
        return False