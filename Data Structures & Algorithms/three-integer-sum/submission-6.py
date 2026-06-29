class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach: After sorting the array, we can fix one number and then search for the other two using the two-pointer technique.
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            # Break if positive values for i, since they cannot sum up to 'zero' anymore
            if nums[i] > 0:
                break
            # If the number is same as previous number, skip this iteration to avoid duplicate
            if nums[i] == nums[i - 1] and i > 0:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                    if nums[j] + nums[k] == -nums[i]:
                        triplet = [nums[i], nums[j], nums[k]]
                        result.append(triplet)
                        j += 1
                        k -= 1
                        # If the number is same as previous number, skip this iteration to avoid duplicate
                        while nums[j] == nums[j - 1] and j < k:
                            j += 1
                    elif nums[j] + nums[k] > -nums[i]:
                        k -= 1
                    elif nums[j] + nums[k] < -nums[i]:
                        j += 1
        return result