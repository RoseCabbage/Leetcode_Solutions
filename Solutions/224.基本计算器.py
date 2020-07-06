#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#
# https://leetcode-cn.com/problems/basic-calculator/description/
#
# algorithms
# Hard (38.02%)
# Likes:    218
# Dislikes: 0
# Total Accepted:    15.7K
# Total Submissions: 41.2K
# Testcase Example:  '"1 + 1"'
#
# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
# 
# 字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。
# 
# 示例 1:
# 
# 输入: "1 + 1"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: " 2-1 + 2 "
# 输出: 3
# 
# 示例 3:
# 
# 输入: "(1+(4+5+2)-3)+(6+8)"
# 输出: 23
# 
# 说明：
# 
# 
# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval。
# 
# 
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        num = 0
        ans = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                ans += num * sign
                num = 0
                sign = 1
            elif char == '-':
                ans += num * sign
                num = 0
                sign = -1
            elif char == '(':
                stack.append(ans)
                stack.append(sign)
                sign = 1
                ans  = 0
            elif char == ')':
                ans += num * sign
                num = 0
                ans = stack.pop() * ans + stack.pop()
        ans += num * sign
        return ans

        # num_stack = []
        # ops_stack = []
        # for char in s:
        #     if char == ' ':
        #         pass
        #     elif char not in ['(', ')', '[', ']']:
        #         num_stack.append(int(char))
        #     elif char != ')':
        #         ops_stack.append(char)
        #     else:
        #         while ops_stack[-1] != '(':
        #             cur = ops_stack.pop()
        #             if cur == '+':
        #                 num1 = num_stack.pop()
        #                 num2 = num_stack.pop()
        #                 num_stack.append(num1 + num2)
        #             elif cur == '-':
        #                 num2 = num_stack.pop()
        #                 num1 = num_stack.pop()
        #                 num_stack.append(num1 - num2)
        #         ops_stack.pop()
        # print(num_stack)
        # print(ops_stack)
        # while ops_stack:
        #     cur = ops_stack.pop()
        #     if cur == '+':
        #         num1 = num_stack.pop()
        #         num2 = num_stack.pop()
        #         num_stack.append(num1 + num2)
        #     else:
        #         num2 = num_stack.pop()
        #         num1 = num_stack.pop()
        #         num_stack.append(num1 - num2)
        # return num_stack[0]


# @lc code=end

