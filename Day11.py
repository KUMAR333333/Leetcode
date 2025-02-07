class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        s=""
        f = strs[0]
        l = strs[-1]
        for i in range(min(len(f),len(l))):
            if f[i] == l[i]:
                s+=f[i]
            
        return s
        
