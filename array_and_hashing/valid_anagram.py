class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def ind(s: str) -> int:
            return ord(s) - ord("a")

        sc, tc = [0] * 26, [0] * 26
        for cs in s:
            sc[ind(cs)] += 1

        for ct in t:
            tc[ind(ct)] += 1

        for i in range(26):
            if sc[i] != tc[i]:
                return False

        return True
