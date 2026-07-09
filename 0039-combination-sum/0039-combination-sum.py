class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        #i = candidates we can still choose, cur = list of values we've added to the current combination
        #total = total sum of values to see if it reaches or goes over target
        def dfs(i, cur, total):
            if total == target: #base case where we succeed
                res.append(cur[:])  #copy cause we modify cur
                return
            if i >= len(candidates) or total > target:
                return
            
            #TWO-BRANCH-DECISION
            #Choose to include the value at candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            #Choose to not include the value at candidates[i]
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res