#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        k %= len(nums)
        swap(0, len(nums) - k - 1)
        swap(len(nums) - k, len(nums) - 1)
        swap(0, len(nums) - 1)

# @lc code=end

