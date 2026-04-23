class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        nums.sort()

        output = []
        for index in range(len(nums)):

            left = index + 1
            right = len(nums) - 1

            
            while left < right:
                if index > 0 and nums[index] == nums[index-1]:
                    left += 1
                    continue
                sum = (nums[index] + nums[left] + nums[right])
                if sum == 0:
                    output.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    if nums[left] == nums[left-1]:
                        left += 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1

                elif sum < 0:
                    left += 1
                    if nums[left] == nums[left-1]:
                        left += 1
                else:
                    right -= 1
                    if nums[right] == nums[right+1]:
                        right -= 1
        
        return output

