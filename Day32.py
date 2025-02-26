class Solution:
    def maxAbsoluteSum(self, nums):
        sum_, minsum, maxsum = 0, 0, 0
        for num in nums:
            sum_ += num
            maxsum = max(maxsum, sum_)
            minsum = min(minsum, sum_)
        return abs(maxsum - minsum)
