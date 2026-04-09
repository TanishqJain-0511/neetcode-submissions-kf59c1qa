class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        x_dict = {}
        for num in nums:
            x_dict[num] = x_dict.get(num, 0) + 1
        
        freq_list = [[] for i in range(0, len(nums)+1)]
        for num, freq in x_dict.items():
            freq_list[freq].append(num)

        result = []
        for n in range(len(freq_list), -1, -1):
            for num in freq_list[n-1]:
                result.append(num)
                if len(result) == k:
                    return result
