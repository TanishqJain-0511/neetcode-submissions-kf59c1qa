class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x_dict = {}
        for index, num in enumerate(nums):
            x_dict[num] = index
        
        for index, num in enumerate(nums):
            remainder = target - num
            if remainder in x_dict and x_dict[remainder] != index:
                return [index, x_dict[remainder]]
