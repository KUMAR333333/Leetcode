class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxy = 0
        for i in range(len(accounts)):
            maxx = 0
            for j in range(len(accounts[0])):
                maxx += accounts[i][j]
            maxy = max(maxy, maxx)
        return maxy
