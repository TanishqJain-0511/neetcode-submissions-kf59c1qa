class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in seen:
                j = seen[remainder]
                return [min(i,j), max(i,j)]
            seen[num] = i
        