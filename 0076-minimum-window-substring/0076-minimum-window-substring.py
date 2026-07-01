class Solution(object):
    def minWindow(self, s, t):
        if t == "":
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = float("infinity")
        l = 0

        # r tells us the right boundary of our current window
        for r in range(len(s)):
            c = s[r]  # get the character we just reached
            window[c] = 1 + window.get(c, 0)  # add c to the window

            if c in countT and window[c] == countT[c]:  # we satisfy a condition
                have += 1

            while have == need:
                if (r - l + 1) < resLen:  # update our result
                    res = [l, r]  # this is the window
                    resLen = (r - l + 1)  # length is the size of the window
                window[s[l]] -= 1  # keep shrinking from left
                if s[l] in countT and window[s[l]] < countT[s[l]]:  # update have count
                    have -= 1
                l += 1

        # We're taking characters adding it to the window map,
        # checking if the condition is met
        # and updating the window accordingly
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""