import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = collections.defaultdict(list)

        for str in strs:
            s = sorted(str)
            hash_map["".join(s)].append(str)

        return hash_map.values()
