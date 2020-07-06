#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (30.67%)
# Likes:    783
# Dislikes: 0
# Total Accepted:    74.3K
# Total Submissions: 232.3K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = []
        match = {']':'[', ')':'(', '}':'{'}
        for idx in range(len(s)):
            if idx == 0:
                dp.append(0)
            else:
                if s[idx] in ['(', '[', '{']:
                    dp.append(0)
                else:
                    temp = 0
                    flag = 0
                    if idx - dp[-1] - 1 >= 0 and s[idx - dp[-1] - 1] == match[s[idx]]:
                        flag = 1
                        temp = dp[-1] + 2 + dp[idx - dp[-1] - 2] if idx - dp[-1] - 2 >= 0 else dp[-1] + 2
                    if idx - 1 >= 0 and match[s[idx]] == s[idx - 1]:
                        flag = 1
                        temp = max(dp[-2] + 2, temp) if len(dp) >= 2 else max(0, temp)
                    if flag == 1:
                        dp.append(temp)
                    else:
                        dp.append(0)
        # print(dp)
        return max(dp)
# @lc code=end

