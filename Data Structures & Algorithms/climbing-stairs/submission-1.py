class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 1 -> 1
        # n = 2 -> 2
        # n = 3 -> 3
        # n = 4 => (n=2) + (n=3) cases so -> 5
        prev = 1 # n=1 case
        curr = 2 # n=2 case

        if n == 1:
            return prev
        elif n == 2:
            return curr
        
        for i in range(n-2):
            prev, curr = curr, prev+curr
        
        return curr