class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        x_dict = {}
        for word in strs:
            if str(sorted(list(word))) not in x_dict.keys():
                x_dict[str(sorted(list(word)))] = [word]
            else:
                x_dict[str(sorted(list(word)))].append(word)
        for value in x_dict.values():
            output.append(value)
        return output
        