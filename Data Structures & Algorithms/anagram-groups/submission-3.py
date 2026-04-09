class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_dict = {}
        
        for word in strs:
            if str(sorted(word)) not in word_dict:
                word_dict[str(sorted(word))] = [word]
            else:
                word_dict[str(sorted(word))].append(word)
        
        output_list = []
        for key, value in word_dict.items():
            output_list.append(value)
        
        return output_list