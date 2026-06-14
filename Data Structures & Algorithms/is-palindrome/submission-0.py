class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for c in s:
            if c.isalnum():
                cleaned+=c.lower()

        length=len(cleaned)
        for i in range(length//2):
            if cleaned[i]!=cleaned[length-i-1]:
                return False
        return True
        