class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = 1

        area = 0

        for i in range(0, len(heights)):

            for j in range(i, len(heights)):

                area = max(area, (j-i)*min(heights[i], heights[j]))

        return area