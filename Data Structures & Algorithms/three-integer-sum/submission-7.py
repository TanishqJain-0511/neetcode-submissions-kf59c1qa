class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = set()
        nums.sort()

        for i in range(0, len(nums)//2+1):

            left = i+1
            right = len(nums)-1

            while left < right:
                sum = (nums[i] + nums[left] + nums[right])
                if sum==0:
                    output.add((nums[i], nums[left], nums[right]))
                    left+=1
                elif sum < 0:
                    left+=1
                else:
                    right-=1
        result = []
        for ele in output:
            result.append(list(ele))

        return result


        


