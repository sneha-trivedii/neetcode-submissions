class Solution:
    def trap(self, height: List[int]) -> int:
        # Approach: Use two pointers from opposite directions. Move pointers only when a greater number occurs and calculate area same as previous solution.
        leftMax, rightMax = 0, 0
        left, right = 0, len(height) - 1
        total = 0
        while left != right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] <= height[right]:
                total = total + (min(leftMax, rightMax) - height[left])
                left += 1
            else:
                total = total + (min(leftMax, rightMax) - height[right])
                right -= 1
        return total