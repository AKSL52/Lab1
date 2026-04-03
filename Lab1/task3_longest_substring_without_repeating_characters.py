class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1] * 128
        left = 0
        max_len = 0

        for right, c in enumerate(s):
            left = max(left, last_seen[ord(c)] + 1)

            last_seen[ord(c)] = right

            max_len = max(max_len, right - left + 1)

        return max_len