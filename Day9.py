class Solution:
    def isBalanced(self, n: str) -> bool:
        a=list(n)
        #print(a)
        sum1=0
        sum2=0
        for i in range(len(a)):
            if i%2==0:
                sum1+=int(a[i])
            else:
                sum2+=int(a[i])
        if sum1==sum2:
            return True
        return False
