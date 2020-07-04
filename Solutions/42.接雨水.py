#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (51.17%)
# Likes:    1413
# Dislikes: 0
# Total Accepted:    116.2K
# Total Submissions: 225.5K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        while left + 1 < right and height[left] == 0:
            left += 1
        while right - 1 > left and height[right] == 0:
            right -= 1
        res = 0
        while left < right:
            cur = left + 1
            while cur < len(height) and height[cur] < height[left]:
                cur += 1
            if cur <= right:
                for i in range(left + 1, cur):
                    res += (height[left] - height[i])
                    # print(res)
                left = cur
            else:
                while left < right:
                    cur = right - 1
                    while cur >= 0 and height[cur] < height[right]:
                        cur -= 1
                    if cur >= left:
                        for i in range(cur + 1, right):
                            res += (height[right] - height[i])
                            # print(res)
                        right = cur
        return res
            

# @lc code=end

