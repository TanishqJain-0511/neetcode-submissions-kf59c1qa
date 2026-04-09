class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for ch in s:
            if ch.isalnum():
                x += ch.lower()
        midpoint = len(x)//2
        second_half = x[midpoint+1:] if len(x)%2!=0 else x[midpoint:]
        reverse_second_half = second_half[::-1]
        return x[0: midpoint] == reverse_second_half