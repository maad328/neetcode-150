from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for c in strs:
            count=[0]*26
            for ch in c:
                count[ord(ch)-ord('a')]+=1
            key=tuple(count)
            group[key].append(c)
        return list(group.values())

            

        