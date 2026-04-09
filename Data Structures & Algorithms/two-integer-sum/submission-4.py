class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for index in range(len(nums)):
            remainder = target - nums[index]
            if remainder in seen:
                return [seen[remainder], index]
            seen[nums[index]] = index