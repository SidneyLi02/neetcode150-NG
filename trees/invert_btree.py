# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # DFS recursive
        if root == None:
            return root
        else:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
        
        # Iterative
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
                curr.left, curr.right = curr.right, curr.left
                stack.append(curr.left)
                stack.append(curr.right)
        return root

        """
        NOTE: 
        solution:                     O(n) time, O(1) space
        iterative:                    O(n) time, O(n) space
        """