class Solution:
    def buttonWithLongestTime(self, a: List[List[int]]) -> int:
        l=[a[0][1]]

        for i in range(1,len(a)):
            b=a[i][1]-a[i-1][1]
            l.append(b)
        maxx=max(l)

        li=[]
        for i in range(len(l)):
            if l[i]==maxx:
                li.append(i)

        lis = [] 
        for i in li:  
            lis.append(a[i][0])  
        return (min(lis))
