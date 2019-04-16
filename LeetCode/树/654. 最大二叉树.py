# 给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
#
# 二叉树的根是数组中的最大元素。
# 左子树是通过数组中最大值左边部分构造出的最大二叉树。
# 右子树是通过数组中最大值右边部分构造出的最大二叉树。
# 通过给定的数组构建最大二叉树，并且输出这个树的根节点。
from 树.traverse import LevelOrder
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:nums.index(root.val)])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(root.val)+1:])
        return root

l = [3,2,1,6,0,5]
s = Solution()
LevelOrder(s.constructMaximumBinaryTree(l))
