# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root:TreeNode)->int:
            if root == None:
                return 0
            lt=check(root.left)
            rt=check(root.right)
            if lt ==-1 or rt==-1 or abs(lt-rt)>1:
                return -1
            return 1+ max(lt,rt)
        if root == None:
            return True
        return check(root)!=-1