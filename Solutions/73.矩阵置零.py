#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
# https://leetcode-cn.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (55.48%)
# Likes:    245
# Dislikes: 0
# Total Accepted:    44.4K
# Total Submissions: 79.8K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
# 
# 示例 1:
# 
# 输入: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# 输出: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# 示例 2:
# 
# 输入: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# 输出: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 进阶:
# 
# 
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？
# 
# 
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            row_flag = 0
            col_flag = 0
            for idx in range(n):
                if matrix[0][idx] == 0:
                    row_flag = 1
                    break
            for idx in range(m):
                if matrix[idx][0] == 0:
                    col_flag = 1
                    break
            for row_idx in range(m):
                for col_idx in range(n):
                    if matrix[row_idx][col_idx] == 0:
                        matrix[row_idx][0] = 0
                        matrix[0][col_idx] = 0
            # print(matrix)
            if m > 1:
                for row_idx in range(1, m):
                    if matrix[row_idx][0] == 0:
                        matrix[row_idx] = [0] * n
            if n > 1:
                for col_idx in range(1, n):
                    if matrix[0][col_idx] == 0:
                        for row_idx in range(m):
                            matrix[row_idx][col_idx] = 0
            if row_flag:
                matrix[0] = [0] * n
            if col_flag:
                for row_idx in range(m):
                    matrix[row_idx][0] = 0
# @lc code=end

