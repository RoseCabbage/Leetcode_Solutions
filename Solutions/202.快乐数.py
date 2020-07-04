#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # hash_set = set()
        # while 1:
        #     n = sum([int(i) ** 2 for i in str(n)])
        #     if n == 1:
        #         return True
        #     elif n in hash_set:
        #         return False
        #     else:
        #         hash_set.add(n)

        #2020.7.3
        history = []
        while 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n == 1:
                return True
            if n in history:
                return False
            else:
                history.append(n)

        
# @lc code=end

