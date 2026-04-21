class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        print(seen)

        output = [[] for i in range(len(nums))]

        for key, value in seen.items():
            output[value-1].append(key)
        
        result = []
        for i in range(len(nums)-1, -1, -1):
            if len(result) >= k:
                return result
            for q in output[i]:
                result.append(q)
                if len(result) >= k:
                    return result