#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (42.57%)
# Likes:    371
# Dislikes: 0
# Total Accepted:    72.4K
# Total Submissions: 162.9K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s
# 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。
# 
# 
# 
# 示例：
# 
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 
# 
# 
# 
# 进阶：
# 
# 
# 如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
# 
# 
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        import math
        if not nums:
            return 0
        cur = begin = 0
        minlen = math.inf
        flag = 0
        for end in range(len(nums)):
            cur += nums[end]
            if cur >= s:
                while begin + 1 <= end and cur - nums[begin] >= s:
                    cur -= nums[begin]
                    begin += 1
                curlen = end - begin + 1
                if curlen < minlen:
                    minlen = curlen
                    flag = 1
        if flag == 0:
            return 0
        else:
            return minlen



# @lc code=end

