class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if not len(s) == len(t):
            return False
        
        s_dict = {}
        for ch in s:
            s_dict[ch] = s_dict.get(ch,0) + 1

        t_dict = {}
        for ch in t:
            t_dict[ch] = t_dict.get(ch,0) + 1
        
        if not s_dict == t_dict:
            return False

        return True