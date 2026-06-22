class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            Approach: Store the frequency of each integer in a hash map
            in descending order and then return the first k values.
        '''

        intFreq = {}

        for number in nums:
            if number in intFreq:
                intFreq[number] += 1
            else:
                intFreq[number] = 1

        # Sorted integers in descending order of frequency
        answer = [
            key
            for key, value in sorted(intFreq.items(), key = lambda item: item[1], reverse = True)]
        return answer[:k]