class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nset = set(nums)
        n = min(nums)
        counts = [0]
        for n in nums:
            if n-1 not in nset: # if n is the start of a seq
                c = 1
                while n+1 in nset: # while the next n is in the st
                    n += 1 # need to update it to check for next
                    c += 1
                counts.append(c)
            else:
                n += 1
        return max(counts)

