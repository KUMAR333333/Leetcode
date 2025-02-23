class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ans = 0
        for c in range(len(grid[0])):  
            for r in range(1, len(grid)):  
                if grid[r][c] <= grid[r - 1][c]:  
                    ans += grid[r - 1][c] + 1 - grid[r][c]  
                    grid[r][c] = grid[r - 1][c] + 1  
        return ans
