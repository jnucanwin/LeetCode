# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if nums == []:
            return None
        nums.sort()
        k = int(len(nums) / 2)
        root = TreeNode(nums[k])
        root.left = self.sortedArrayToBST(nums[0:k])
        root.right = self.sortedArrayToBST(nums[k + 1:])
        return root
