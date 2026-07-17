# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        res = root.val
        def inorder(root):
            nonlocal counter, res
            if not root:
                return
            inorder(root.left)
            counter -= 1
            if counter == 0:
                res = root.val
                return
            inorder(root.right)
        inorder(root)
        return res