class Solution:
    def tribonacci(self, n: int) -> int:
        savelist=[0,1,1]
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        summ=0
        if n>2 and n <=37:
            for i in range(3,n+1):
                summ = savelist[i-1]+savelist[i-2]+savelist[i-3]
                savelist.append(summ)
            return summ