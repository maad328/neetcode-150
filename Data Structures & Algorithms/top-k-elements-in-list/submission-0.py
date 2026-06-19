from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1

        freq=[[] for i in range(len(nums)+1)]
        for x,y in count.items():
            freq[y].append(x)
        result=[]
        for i in range(len(freq) -1, 0, -1):
            for x in freq[i]:
                result.append(x)
                if len(result)==k:
                    return result