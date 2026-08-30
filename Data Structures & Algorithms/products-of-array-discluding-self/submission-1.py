class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = []
        for i in range(len(nums)):
            prefix.append(product)
            product*=nums[i]

        suffix = []
        # slicing always best for reversing list
        rev_nums = nums[::-1]
        product = 1
        for i in range(len(rev_nums)):
            suffix.append(product)
            product*=rev_nums[i]
        
        suffix = suffix[::-1]

        output = []
        j = 0

        while j < len(nums):
            output.append(prefix[j]*suffix[j])
            j += 1

        return output