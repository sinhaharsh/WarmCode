"""
LeetCode #1008 : Construct Binary Search Tree from Preorder Traversal
[https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/]
Date: May 2 2022
Notes:
    Used stack to keep track of nodes. Added lower value to left, and searched the stack
    to get the element for adding the right node.
    Watched solution, re-read about Preorder, Inorder and PostOrder traversal.
    [Pre, In, Post] denote the position of the root with respect to left and
    right nodes.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        stack = []
        root = TreeNode(preorder[0])
        n = len(preorder)
        stack.append(root)

        for i in range(1, n):
            # print(i, preorder[i])
            if preorder[i] < stack[-1].val:
                stack[-1].left = TreeNode(preorder[i])
                stack.append(stack[-1].left)
            else:
                while stack and preorder[i] > stack[-1].val:
                    last = stack.pop()
                last.right = TreeNode(preorder[i])
                stack.append(last.right)
        return root