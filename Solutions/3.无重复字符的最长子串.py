#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (34.66%)
# Likes:    3891
# Dislikes: 0
# Total Accepted:    544.1K
# Total Submissions: 1.6M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin = 0
        end = -1
        curLen = 0
        curList = []
        maxLen = 0
        while end < len(s) - 1:
            end += 1
            if s[end] not in curList:
                curList.append(s[end])
                curLen += 1
            else:
                while s[begin] != s[end]:
                    begin += 1
                begin += 1
                curLen = end - begin + 1
                curList = list(s[begin:end+1])
            if curLen > maxLen:
                maxLen = curLen
        return maxLen
# @lc code=end

