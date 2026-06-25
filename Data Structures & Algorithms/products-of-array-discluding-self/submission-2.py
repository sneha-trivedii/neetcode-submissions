class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            Prefix-Suffix Approach: Maintain a HashMap with prefix products (excluding the number itself) as keys and suffix products (excluding the number) as values. For the result, multiply respective keys and values.
        '''
        preArr, sufArr = [], []
        # Prefix List Formation
        product = 1
        for i in range(len(nums)):
            if i == 0:
                product = 1
            else:
                product = preArr[i - 1] * nums[i - 1]
            preArr.append(product)
        # Suffix List Formation
        product = 1
        for i in reversed(range(len(nums))):
            if i == (len(nums) - 1):
                product = 1
            else:
                product = sufArr[len(nums) - i - 2] * nums[i + 1]
            sufArr.append(product)
        # Reverse suffix list
        sufArr.reverse()
        # Multiply prefix and suffix list to get answer array
        answer = []
        for i in range(len(nums)):
            answer.append(preArr[i] * sufArr[i])
        return answer