class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}

        for i,x in enumerate(nums):
            diff = target - nums[i]
            if diff not in ref:
                ref[x] = i
            else: # if diff in ref
                return(sorted([ref[diff], i]))