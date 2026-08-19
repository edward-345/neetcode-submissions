class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dic = {key: value}
        # keys have to be unique not values
        # both the values in nums and the target can be negative
        ref = {}
        for x,y in enumerate(nums): # x is indice y is value
            diff = target - y
            # remember you can only refer to values via keys 
            if diff not in ref: # if difference not in ref keys
                ref[y] = x # that number is key for its list indice
            elif diff in ref:
                return(sorted([x, ref[diff]]))
