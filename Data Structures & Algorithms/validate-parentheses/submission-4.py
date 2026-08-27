class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for b in s:
            if b in pairs.values():
                stack.append(b)
            elif b not in pairs.values():
                if not stack or stack[-1] != pairs[b]:
                    return False
                else:
                    stack.pop()
            
        return not stack


        