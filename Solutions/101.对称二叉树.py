#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (52.15%)
# Likes:    889
# Dislikes: 0
# Total Accepted:    170.3K
# Total Submissions: 325.3K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# 进阶：
# 
# 你可以运用递归和迭代两种方法解决这个问题吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMirror(self, tree1: TreeNode, tree2: TreeNode) -> bool:
        if not tree1:
            if tree2:
                return False
            else:
                return True
        if not tree2:
            if tree1:
                return False
            else:
                return True
        return tree1.val == tree2.val and self.isMirror(tree1.left, tree2.right) and self.isMirror(tree1.right, tree2.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
        
# @lc code=end

