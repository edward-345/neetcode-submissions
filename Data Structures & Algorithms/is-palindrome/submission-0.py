class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(ch for ch in s if ch.isalnum()).lower()
        rev = word[::-1]
        return rev == word