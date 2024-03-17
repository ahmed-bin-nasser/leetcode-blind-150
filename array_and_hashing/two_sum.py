from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nc: dict[int, int] = {}
        for i, n in enumerate(nums):
            if (ind := nc.get(target - n, None)) is not None:
                return [ind, i]
            nc[n] = i

        return []
