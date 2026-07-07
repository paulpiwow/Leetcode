# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        def validate(node, min_val, max_val):
            if not node:                          # empty node is valid
                return True
            if node.val >= max_val:               # violated upper boundary
                return False
            if node.val <= min_val:               # violated lower boundary
                return False
            
            return (validate(node.left, min_val, node.val) and   # go left, update max
                    validate(node.right, node.val, max_val))      # go right, update min
        
        return validate(root, float("-inf"), float("inf"))        # start with no boundaries