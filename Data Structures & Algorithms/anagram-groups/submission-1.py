class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        x_dict = {}
        for word in strs:
            if str(sorted(list(word))) not in x_dict.keys():
                x_dict[str(sorted(list(word)))] = [word]
            elif str(sorted(list(word))) in x_dict.keys():
                x_dict[str(sorted(list(word)))].append(word)
        for key, value in x_dict.items():
            output.append(value)
        return output
        