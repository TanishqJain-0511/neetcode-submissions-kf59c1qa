class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        temp = {}
        for ch in s:
            temp[ch] = temp.get(ch,0) + 1
        
        temp_2 = {}
        for ch in t:
            if ch not in temp:
                return False
            temp_2[ch] = temp_2.get(ch, 0) + 1
        
        return temp == temp_2