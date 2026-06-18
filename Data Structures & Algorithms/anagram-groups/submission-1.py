from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for x in strs:
            ch=[0]*26
            for s in x:
                ch[ord(s)-ord('a')]+=1
            key=tuple(ch)
            group[key].append(x)
        return list (group.values())


        

            

        