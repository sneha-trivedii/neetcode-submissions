class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            Approach: Using Bucket List. We can use this idea by
            creating a list where the index represents a frequency,
            and at each index we store all numbers that appear
            exactly that many times.
        '''

        freqList = [[] for i in range(len(nums) + 1)]
        freqMap = {}
        for number in nums:
            freqMap[number] = 1 + freqMap.get(number, 0)
        for key, value in freqMap.items():
            if freqList[value] == 0:
                freqList[value] = key
            else:
                [freqList[value].append(key)]
        # add the non-zero items in another list in descending
        # order and extract the 1st k elements from the new list.
        answer = []
        for item in freqList[::-1]:
            if len(item) != 0:
                answer.extend(item)
        return answer[:k]



        