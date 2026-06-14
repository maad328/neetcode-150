class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count={}
        for i,num in enumerate(numbers):
            second=target-num
            if second in count:
                return [count[second],i+1]
            count[num]=i+1


        