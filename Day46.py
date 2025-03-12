class Solution:
    def maximumCount(self, nums):
        posc = 0
        negc = 0
        for num in nums:
            if num < 0:
                negc += 1
            elif num > 0:
                posc += 1
        return max(negc, posc)
