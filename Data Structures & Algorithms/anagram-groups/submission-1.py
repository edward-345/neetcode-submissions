class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ref = {sorted string: [list of anagrams that have same sorted string]}
        ref = {}

        for i,s in enumerate(strs):
            srted = "".join(sorted(s))
            if srted not in ref:
                ref[srted] = [s]
            elif srted in ref:
                ref[srted].append(s)
        
        # need to turn ref into list

        return(list(ref.values()))  
  