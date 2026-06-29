class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Approach: Use two pointers to calculate area. Move the pointer with lesser height inward.
        area = 0
        i, j = 0, len(heights) - 1
        while i < j:
            currArea = min(heights[i], heights[j]) * (j - i)
            if currArea > area:
                area = currArea
            if heights[j] > heights[i]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
                j -= 1
        return area

