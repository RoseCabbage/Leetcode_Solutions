#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (40.48%)
# Likes:    410
# Dislikes: 0
# Total Accepted:    66.7K
# Total Submissions: 163.9K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
# 
# 示例 1:
# 
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2:
# 
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        n = len(matrix[0])
        ans = []
        flag = 0
        while matrix != [] and n != 0:
            if flag % 4 == 0:
                ans += matrix.pop(0)
            if flag % 4 == 1:
                n -= 1
                for each in matrix:
                    ans.append(each.pop())
            if flag % 4 == 2:
                ans += matrix.pop(-1)[::-1]
            if flag % 4 == 3:
                n -= 1
                for idx in range(len(matrix) - 1, -1, -1):
                    ans.append(matrix[idx].pop(0))
            flag += 1
        return ans




# @lc code=end

