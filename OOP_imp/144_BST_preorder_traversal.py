# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # def preorderTraversal(self, root):
    #
    #     def traversal(node):
    #         if not node:
    #             return
    #
    #         order_list.append(node.val)
    #         traversal(node.left)
    #         traversal(node.right)
    #
    #     order_list = [root]
    #     traversal(root)
    #
    #     return ordered_list

    # iterative solution for pre-order traversal
    def preorderTraversal(self, root):
        stack = [root]
        result = []

        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return result


_obj = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)

_obj.preorderTraversal(root)
