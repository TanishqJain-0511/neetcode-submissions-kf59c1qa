class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        if len(s) <= 2:
            return True
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                l1 = left + 1
                r1 = right
                l2 = left
                r2 = right-1
                left_ok = True
                right_ok = True
                while l1 < r1:
                    if s[l1] != s[r1]:
                        left_ok = False
                    l1 +=1 
                    r1 -=1

                while l2 < r2:
                    if s[l2] != s[r2]:
                        right_ok = False
                    l2 +=1 
                    r2 -=1
                return left_ok or right_ok
        return True