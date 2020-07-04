#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (44.18%)
# Likes:    502
# Dislikes: 0
# Total Accepted:    131.3K
# Total Submissions: 286.8K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 
# 
# 示例：
# 
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        import math
        curval = math.inf
        bestval = math.inf
        nums.sort()
        for i in range(len(nums)):
            if 3 * nums[i] - target > math.fabs(bestval - target):
                return bestval
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curval = nums[i] + nums[left] + nums[right]
                if curval == target:
                    return target
                elif curval > target:
                    if math.fabs(curval - target) < math.fabs(bestval - target):
                        bestval = curval
                    while right - 1 >= 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    if right - 1 >= 0:
                        right -= 1
                else:
                    if math.fabs(curval - target) < math.fabs(bestval - target):
                        bestval = curval
                    while left + 1 < len(nums) and nums[left] == nums[left + 1]:
                        left += 1
                    if left + 1 < len(nums):
                        left += 1
        return bestval

# @lc code=end

