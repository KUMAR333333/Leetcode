class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = rowIndex + 1
        ans = []
        res = 1
        ans.append(res)
        
        for i in range(1, row):
            res = res * (row - i) // i 
            ans.append(res)
        
        return ans

    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for i in range(numRows):
            answer.append(self.getRow(i))
        return answer
