class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 1
        temp = 0
        for right in range(1, len(nums)):
            left = right - 1
            while left >= temp:
                if nums[right] & nums[left]:
                    break
                left -= 1
            temp  =left + 1
            res = max(res, right - temp + 1)

        return res
