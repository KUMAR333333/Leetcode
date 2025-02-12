class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=[]
        self.backtrack(l,"",0,0,n)
        return l
    def backtrack(self,l : List[str],s : str,open : int,close : int,n : int):
        if(len(s) == n*2):
            l.append(s)
            return
        if(open < n):
            self.backtrack(l,s+"(",open + 1,close,n)
        if(close < open):
            self.backtrack(l,s+")",open,close+1,n)
    
