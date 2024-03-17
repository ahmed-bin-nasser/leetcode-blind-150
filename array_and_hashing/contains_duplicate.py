from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map: dict[int, bool] = {}
        for n in nums:
            if hash_map.get(n, False):
                return True

            hash_map[n] = True
        return False
