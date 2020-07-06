#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
# https://leetcode-cn.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (38.90%)
# Likes:    180
# Dislikes: 0
# Total Accepted:    14.8K
# Total Submissions: 37.4K
# Testcase Example:  '"bcabc"'
#
# 给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
# 
# 
# 
# 示例 1:
# 
# 输入: "bcabc"
# 输出: "abc"
# 
# 
# 示例 2:
# 
# 输入: "cbacdcbc"
# 输出: "acdb"
# 
# 
# 
# 注意：该题与 1081
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
# 相同
# 
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        dic = Counter(s)
        visited = set()
        stack = []
        for char in s:
            if char in visited:
                dic[char] -= 1
                continue
            while stack and char < stack[-1] and dic[stack[-1]] > 1:
                cur = stack.pop()
                dic[cur] -= 1
                visited.remove(cur)
            stack.append(char)
            visited.add(char)
        return ''.join(stack)

# @lc code=end

