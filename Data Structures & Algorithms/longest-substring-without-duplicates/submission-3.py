class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        x = []
        
        output = 0

        left, right = 0, 0

        while right < len(s):
            if s[right] not in x:
                x.append(s[right])
                
            else:
                while s[right] in x:
                    x.pop(0)
                    left += 1
                x.append(s[right])
                
            right += 1
            output = max(output, right-left)
        return output 
            
