class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        curr = 2

        if n == 1:
            return prev
        elif n == 2:
            return 2

        for i in range(n - 2):
            s = curr + prev
            prev,curr = curr,(curr+prev)

        return s