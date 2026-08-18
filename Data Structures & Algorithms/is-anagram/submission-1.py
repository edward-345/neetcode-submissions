class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # has to be exact same chars same number of times
        return sorted(s) == sorted(t)