class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
       
        temp = {}

        for word in strs:
            x = [0]*26
            for ch in word:
                x[ord(ch.lower()) - ord("a")] += 1
            if tuple(x) not in temp:
                temp[tuple(x)] = [word]
            else:
                temp[tuple(x)].append(word)
        
        output = []
        for key, value in temp.items():
            output.append(value)
        return output
