class Solution:
    def countPrefixSuffixPairs(self, w: List[str]) -> int:
        c=0
        for i in range(len(w)):
            for j in range(i+1,len(w)):
                if w[j].startswith(w[i]) and w[j].endswith(w[i]):
                    c+=1
        return c
                
