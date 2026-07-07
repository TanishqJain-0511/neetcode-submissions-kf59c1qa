class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights)-1

        area = min(heights[left], heights[right])*(right-left)

        while left != right-1:

            if heights[left] >= heights[right]:
                right -= 1
                
            else:
                left += 1
            area = max(area, min(heights[left], heights[right])*(right-left))
        return area