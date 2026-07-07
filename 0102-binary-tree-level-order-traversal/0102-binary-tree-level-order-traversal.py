# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        res = []
        q = collections.deque()
        q.append(root) 

        while q:
            qLen = len(q) #ensures we go one level at a time
            level = []  #for each level
            for i in range(qLen): #loop through every value in the current queue
                node = q.popleft()  #FIFO
                if node:    #node could be null
                    level.append(node.val) #append this node to it's level
                    q.append(node.left) #append children
                    q.append(node.right)
            if level: #only append if the level is non-empty
                res.append(level) 
        return res
