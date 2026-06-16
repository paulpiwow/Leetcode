class Solution(object):
    def longestConsecutive(self, nums):
        hashset = set(nums)
        longest = 0

        for n in hashset:          # iterate the set, not nums
            if (n - 1) not in hashset:
                length = 0
                while (n + length) in hashset:
                    length += 1
                longest = max(length, longest)
        return longest

        