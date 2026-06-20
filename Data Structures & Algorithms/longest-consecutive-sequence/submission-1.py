class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        count={}
        nums.sort()
        for x in nums:
            count[x]=count.get(x-1,0)+1
        maxsequence=0
        for x in count.values():
            if x>maxsequence:
                maxsequence=x
        return maxsequence


        