class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach: After sorting the array, we can fix one number and then search for the other two using the two-pointer technique.
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in result:
                        result.append(triplet)
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
        return result