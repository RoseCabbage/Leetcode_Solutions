#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (34.58%)
# Likes:    333
# Dislikes: 0
# Total Accepted:    30.2K
# Total Submissions: 86.9K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 
# 你找到的子数组应是最短的，请输出它的长度。
# 
# 示例 1:
# 
# 
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
# 
# 
# 说明 :
# 
# 
# 输入的数组长度范围在 [1, 10,000]。
# 输入的数组可能包含重复元素 ，所以升序的意思是<=。
# 
# 
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        right = 0
        maxnum = nums[right]
        for i in range(len(nums)):
            if nums[i] >= maxnum:
                maxnum = nums[i]
            else:
                right = i
        left = len(nums) - 1
        minnum = nums[left]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= minnum:
                minnum = nums[i]
            else:
                left = i
        if right > left:
            return right - left + 1
        else:
            return 0
        
# @lc code=end

