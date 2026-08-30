class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        prev2 = 0

        for n in nums:
            new = max(prev, prev2+n)
            prev2,prev = prev,new
        
        return prev