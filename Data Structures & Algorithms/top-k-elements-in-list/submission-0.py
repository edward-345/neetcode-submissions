class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = {}
        for n in nums: # using numbers in num themselves
            if n not in ref:
                ref[n] = 1 # n is the number as the key, value is their count
            elif n in ref:
                ref[n] += 1
        
        srt = sorted(ref, key=ref.get)
        return srt[-k:]

