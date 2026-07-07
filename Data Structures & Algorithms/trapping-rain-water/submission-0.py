class Solution:
    def trap(self, height: List[int]) -> int:
        # Approach: Maintain leftMax and rightMax (create a suffix list) for each number. For each number, the number should be less than leftMax and rightMax, calculate the minimum of leftMax and rightMax, that minus the height of current number is rain trapped.
        leftMax = 0
        # suffixList
        rightMax = [0 for _ in range(len(height))]
        rightMax[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2 , -1 , -1):
            rightMax[i] = max(height[i], rightMax[i + 1])
        total = 0
        for i in range(len(height)):
            leftMax = max(leftMax, height[i])
            total = total + (min(leftMax, rightMax[i]) - height[i])
        return total
        