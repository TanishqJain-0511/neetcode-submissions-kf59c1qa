class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        set_substring = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in set_substring:
                set_substring.remove(s[left])
                left += 1
            set_substring.add(s[right])
            max_length = max(max_length, len(set_substring))
        return max_length
            