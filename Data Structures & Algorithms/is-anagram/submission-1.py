class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (str(sorted(s)) == str(sorted(t)))