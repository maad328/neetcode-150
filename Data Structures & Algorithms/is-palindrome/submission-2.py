class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for c in s:
            if c.isalnum():
                cleaned+=c.lower()

        r=len(cleaned)-1
        l=0
        while l<r:
            if cleaned[l]!=cleaned[r]:
                return False
            l+=1
            r-=1
        return True
        