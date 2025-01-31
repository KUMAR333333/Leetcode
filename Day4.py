class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        ss = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        s2=""
        for k,v in ss.items():
            s2+=k*v
        return s2
