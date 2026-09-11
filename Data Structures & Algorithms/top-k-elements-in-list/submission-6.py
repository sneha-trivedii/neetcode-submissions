class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Approach: Use bucket sort 
        freq = {}
        for num in nums:
            freq[num] = 1+ freq.get(num, 0)
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in freq.items():
            bucket[value].append(key)
        result = []
        for lis in bucket[::-1]:
            for num in lis:
                result.append(num)
                if len(result) == k:
                    return result