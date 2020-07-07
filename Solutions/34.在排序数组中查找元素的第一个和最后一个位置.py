#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (39.60%)
# Likes:    490
# Dislikes: 0
# Total Accepted:    105.6K
# Total Submissions: 265.1K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 如果数组中不存在目标值，返回 [-1, -1]。
# 
# 示例 1:
# 
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 
# 示例 2:
# 
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        lo = 0
        hi = len(nums) - 1
        center = -1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                center = mid
                break
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        if nums[lo] == target:
            center = lo
        if center == -1:
            return [-1, -1]
        else:
            lo = hi = center
            while lo - 1 >= 0 and nums[lo - 1] == target:
                lo -= 1
            while hi + 1 <= len(nums) - 1 and nums[hi + 1] == target:
                hi += 1
            return [lo, hi]

# @lc code=end

