class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        if len(s) != len(t):
            return False
        else:
            for ch in s:
                if ch in dict_s.keys():
                    dict_s[ch] += 1
                else:
                    dict_s[ch] = 1
            for ch in t:
                if ch in dict_t.keys():
                    dict_t[ch] += 1
                else:
                    dict_t[ch] = 1
            for ch in dict_s.keys():
                if ch not in dict_t.keys():
                    return False
                else:
                    if not (dict_s[ch] == dict_t[ch]):
                        return False
        return True  