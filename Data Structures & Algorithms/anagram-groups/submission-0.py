class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = sorted(strs)
        dic = {}

        for w in words:
            swrd = "".join(sorted(w)) # should set as key 
            if swrd not in dic:
                dic[swrd] = [w]
            elif swrd in dic:
                dic[swrd].append(w)
        
        return list(dic.values())
        