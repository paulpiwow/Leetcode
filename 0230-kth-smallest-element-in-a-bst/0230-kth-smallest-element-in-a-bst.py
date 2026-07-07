# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        #ITERATIVE SOLUTION
        n = 0 #tells us the number of nodes we've visited
        stack = []
        cur = root
    
        while cur or stack:
            while cur:  #while cur is not null keep going left
                stack.append(cur)   #go back up to cur and add it to the stack
                cur = cur.left  #go left

            cur = stack.pop() #pop the most recently added value
            n += 1
            if n == k:
                return cur.val
            cur = cur.right