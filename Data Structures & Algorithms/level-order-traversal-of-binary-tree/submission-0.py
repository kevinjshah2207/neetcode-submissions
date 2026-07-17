# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        if root:
            queue.append(root)
        while queue:
            level = []
            qLen = len(queue)
            for i in range(qLen):
                num = queue.popleft()
                if num:
                    level.append(num.val)
                    queue.append(num.left)
                    queue.append(num.right)
            if level:
                res.append(level)
        return res
