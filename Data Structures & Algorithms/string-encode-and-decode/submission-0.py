class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello","World"]  →  "5#Hello5#World"
        # ["neet","code"]    →  "4#neet4#code"
        enc = ""
        for w in strs:
            tag = str(len(w))+'#'
            enc+=tag+w
        return enc

    def decode(self, s: str) -> List[str]:
        # the reverse direction
        dec = []
        i = 0
        while i < len(s):
            j = i
            if s[j].isdigit() == True:
                while s[j] != "#":
                    j += 1 
                    #necessary for multi digit
                    # now s[i:j] is the length digit
                    # and s[j] is the # character
                lgt = int(s[i:j])
                st = s[j+1:j+1+lgt]
                dec.append(st)
                i = j + 1 + lgt
        return dec
