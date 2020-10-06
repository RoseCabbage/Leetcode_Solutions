#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        flag = [1] * n
        res = 0
        for i in range(2, n):
            if flag[i] == 1:
                res += 1
            j = 2
            while j * i < n:
                flag[i * j] = 0
                j += 1
        return res
            
# @lc code=end

