class Solution(object):
    def isAnagram(self, s, t):
        counterS = Counter(s)
        counterT = Counter(t)
        return counterS == counterT
        