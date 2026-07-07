class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        x_dict = {}

        for i in range( 0, len(nums)):
            remainder = target - nums[i]
            if remainder not in x_dict:
                x_dict[nums[i]] = i
            else:
                return [x_dict[remainder], i]
    