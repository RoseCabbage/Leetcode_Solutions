#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (37.35%)
# Likes:    1127
# Dislikes: 0
# Total Accepted:    301.1K
# Total Submissions: 785.1K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        if len(strs) == 1:
            return strs[0]
        minlen = min([len(each) for each in strs])
        cur = 0
        while cur < minlen:
            letter = strs[0][cur]
            for each in strs:
                if each[cur] != letter:
                    return each[:cur]
            cur += 1
        return strs[0][:cur]

# @lc code=end

