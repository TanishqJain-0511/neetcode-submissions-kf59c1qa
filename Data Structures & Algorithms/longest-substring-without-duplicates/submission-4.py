class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        x = set()
        
        output = 0

        left, right = 0, 0

        while right < len(s):        
            if s[right] in x:
                while s[right] in x:
                    x.remove(s[left])
                    left += 1

            x.add(s[right])
            right += 1
            output = max(output, right-left)
        return output 
            
