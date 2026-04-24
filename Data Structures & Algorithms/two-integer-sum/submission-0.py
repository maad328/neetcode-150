class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count={}
        for i,num in enumerate(nums):
            second=target-num
            if second in count:
                return [count[second],i]
            count[num]=i
        

        