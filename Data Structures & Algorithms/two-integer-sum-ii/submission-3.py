class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while(left<right):
            if numbers[left]+numbers[right]-target==0:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]-target<0:
                left += 1
            elif numbers[left]+numbers[right]-target>0:
                right -= 1
