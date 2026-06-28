class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Approach: Since array is sorted, use two pointers to adjust the sum. If current sum is greater than target, move right pointer to left to make the sum smaller and vice versa
        
        i, j = 0, len(numbers) - 1
        while i < j:
            currSum = numbers[i] + numbers[j]
            if currSum > target:
                j -= 1
            elif currSum < target:
                i += 1
            elif currSum == target:
                return [i + 1, j + 1]
        return[]