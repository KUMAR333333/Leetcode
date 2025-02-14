class Solution:
    def generateSubset(self, index, arr, res, ans):
        ans.append(res[:])
        for i in range(index, len(arr)):
            if i > index and arr[i] == arr[i - 1]:
                continue
            res.append(arr[i])
            self.generateSubset(i + 1, arr, res, ans)
            res.pop()

    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []
        self.generateSubset(0, nums, [], ans)
        return ans
