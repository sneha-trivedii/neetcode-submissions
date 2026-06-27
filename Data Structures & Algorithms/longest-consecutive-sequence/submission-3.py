class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Approach: Sort the array and then look for consecutive subsequence using two pointers
        nums.sort()
        longestSeq, i, j, same = 0, 0, 0, 0
        if i in nums:
            longestSeq = 1
        for number in range(len(nums)):
            try:
                if nums[number] + 1 == nums[number + 1]:
                    j = number + 1
                    longestSeq = max(longestSeq,(j - i + 1 - same))
                elif nums[number] == nums[number + 1]:
                    same += 1
                    j += 1
                else:
                    j += 1
                    i = j
                    same = 0
            except IndexError:
                if len(nums) == 1:
                    longestSeq = 1
                    break
                else:
                    break
        return longestSeq