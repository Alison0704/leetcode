class Solution:
    def pivotInteger(self, n: int) -> int:
        m = []
        for i in range(1,n+1):
            m.append(i)
        for j in range(n):
            if(sum(m[:j+1])==sum(m[j:])):
                return j+1
        return -1
#----------------------------------------------------------------
class Solution:
    def pivotInteger(self, n: int) -> int:
        m = []
        for i in range(1,n+1):
            sum1 = sum(range(1,i+1))
            sum2 = sum(range(i,n+1))
            if(sum1 == sum2):
                return i
        return -1 