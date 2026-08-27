class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        a = 1
        b = 2 
        i = 1
        while i <= (n-2):
            st = a+b
            a = b
            b = st
            i += 1
        
        return(st)
        



        
        