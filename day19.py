class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        next_index = {}
        l = 0

        for r in range(n):
            if s[r] in next_index:
                l = max(next_index[s[r]], l)
            longest = max(longest, r - l + 1)
            next_index[s[r]] = r + 1

        return longest
        
