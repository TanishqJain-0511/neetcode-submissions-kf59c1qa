class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()
        for index in range(len(nums)):
            
            if index > 0 and nums[index-1] == nums[index]:
                continue

            left = index+1
            right = len(nums)-1
            while left < right:
                three_sum = (nums[left] + nums[right] + nums[index])
                if three_sum == 0:
                    output.append([nums[left], nums[index], nums[right]])
                    # Move pointers
                    left += 1


                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
        return output