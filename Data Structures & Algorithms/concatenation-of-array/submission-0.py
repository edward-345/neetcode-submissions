class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copied = nums.copy()
        ans = nums + copied

        return ans