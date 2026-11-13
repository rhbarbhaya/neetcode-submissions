class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        source = {}
        target = {}
        for i in s:
            if i in source.keys():
                source[i] += 1
            else:
                source[i] = 1
        for j in t:
            if j in target.keys():
                target[j] += 1
            else:
                target[j] = 1
        return source == target