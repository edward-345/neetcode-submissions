class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        p = 0
        p2 = 0

        q = 0
        q2 = 0

        n1 = nums[:-1] # first house to second to last house
        n2 = nums[1:]  #second house to last house

        # first house to second last
        for n in n1:
            new = max(p, p2+n)
            p2,p = p,new
        # would return p but we need to compare at the end

        # second house to last 
        for n in n2:
            new = max(q, q2+n)
            q2,q = q, new
        
        return(max(p,q))
