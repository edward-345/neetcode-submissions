class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # gonna need to sort then slice for the k biggest
        import heapq
        ref = {}

        for i,n in enumerate(nums):
            if n not in ref:
                ref[n] = 1
            elif n in ref:
                ref[n]+=1

        # u gotta return the KEYS (unique ints) that have the highest   VALUEs (their frequencies)
        # but max(dict) returns max KEY.. and max(dict.values) finds the max but only returns the value ie their frequency
        return heapq.nlargest(k, ref.keys(), key=ref.get)