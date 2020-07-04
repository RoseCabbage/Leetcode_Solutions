#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (42.32%)
# Likes:    375
# Dislikes: 0
# Total Accepted:    70.4K
# Total Submissions: 166K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 
# 示例 1:
# 
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 
# 示例 2:
# 
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 
# 说明：
# 
# 
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # num1 = num1[::-1]
        # num2 = num2[::-1]
        # carry = 0
        # ans = ''
        # for idx2 in range(len(num2)):
        #     cur = '0' * idx2
        #     for idx1 in range(len(num1)):
        #         temp = int(num2[idx2]) * int(num1[idx1]) + carry
        #         cur += str(temp % 10)
        #         carry = temp // 10
        #     idx = 0
        #     tempcarry = 0
        #     while idx < len(ans) or idx < len(cur) or tempcarry != 0:
        #         newans = ''
        #         x = int(ans[idx]) if idx < len(ans) else 0
        #         y = int(cur[idx]) if idx < len(cur) else 0
        #         new_temp = x + y + carry
        #         newans += str(new_temp % 10)
        #         tempcarry = new_temp // 10
        #     ans = newans
        # return ans[::-1]

        num1 = num1[::-1]
        num2 = num2[::-1]
        res = 0

        for i, x in enumerate(num2):
            temp_res = 0
            for j, y in enumerate(num1):
                temp_res += int(x) * int(y) * 10 ** j
            res += temp_res * 10 ** i

        return str(res)





# @lc code=end

