class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_dict = {}

        for word in strs:
            count = [0]*26

            for ch in word:
                count[ord(ch) - ord("a")] += 1

            if tuple(count) not in word_dict:
                word_dict[tuple(count)] = [word]
            else:
                word_dict[tuple(count)].append(word)
            
        return list(word_dict.values())