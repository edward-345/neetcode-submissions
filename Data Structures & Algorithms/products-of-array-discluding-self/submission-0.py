class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # building prefix list, prod of everything left of each index
        pfx = [1]
        m = pfx[0]
        c = 0
        while c < len(nums)-1:
            pfx.append(m*nums[c])
            m*=nums[c]
            c+=1
        # buidling suffix list, prod of everything right of index
        sfx = [1]
        m = sfx[0]
        c = 0
        rnums = list(reversed(nums))
        while c < len(rnums)-1:
            sfx.append(m*rnums[c])
            m*=rnums[c]
            c+=1
        sfx = list(reversed(sfx))

        output = []
        for i in range(len(nums)):
            output.append(pfx[i]*sfx[i])

        return output
