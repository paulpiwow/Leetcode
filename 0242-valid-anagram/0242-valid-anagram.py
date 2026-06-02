class Solution(object):
    def isAnagram(self, s, t):
        from collections import Counter
        counterS = Counter(s)
        counterT = Counter(t)
        return counterS == counterT
        