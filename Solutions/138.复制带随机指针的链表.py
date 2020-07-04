#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        # cur = head
        # while cur.next:
        #     new = Node(cur.val,None,None)
        #     new.next = cur.next
        #     cur.next = new
        #     cur = cur.next.next
        # cur = head
        # while cur:
        #     if cur.random:
        #         cur.next.random = cur.random.next
        #     cur = cur.next.next
        # ans = head.next
        # cur = ans
        # while cur.next.next:
        #     cur.next = cur.next.next
        #     cur = cur.next
        # return ans
        dic = {}
        cur = head
        while cur:
            if cur not in dic:
                dic[cur] = Node(cur.val, None, None)
            if cur.next:
                if cur.next not in dic:
                    dic[cur.next] = Node(cur.next.val, None, None)
                dic[cur].next = dic[cur.next]
            if cur.random:
                if cur.random not in dic:
                    dic[cur.random] = Node(cur.random.val, None, None)
                dic[cur].random = dic[cur.random]
            cur = cur.next
        return dic[head]
        
        
# @lc code=end

