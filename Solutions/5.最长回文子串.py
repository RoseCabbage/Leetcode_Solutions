#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (30.63%)
# Likes:    2395
# Dislikes: 0
# Total Accepted:    309.9K
# Total Submissions: 1M
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        maxLen = 1
        start = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for hi in range(1, n):
            for lo in range(hi):
                if s[lo] == s[hi]:
                    if hi - lo < 3:
                        dp[lo][hi] = True
                    else:
                        dp[lo][hi] = dp[lo + 1][hi - 1]
                else:
                    dp[lo][hi] = False
                if dp[lo][hi]:
                    curLen = hi - lo +  1
                    if curLen > maxLen:
                        maxLen = curLen
                        start = lo
        return s[start:start + maxLen]

            
# @lc code=end

