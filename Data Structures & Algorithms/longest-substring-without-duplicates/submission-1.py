class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ref = {}
        output = 0
        l = 0

        for i,r in enumerate(s):
            if r in ref and ref[r] >= l:
                l = max(l, ref[r]+1)
            elif r not in ref:
                ref[r] = i
            ref[r] = i
            output = max(output, i-l+1)
        return output