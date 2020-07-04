#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        if k == 0:
            return head
        Node = ListNode(None)
        Node.next = head
        fast = Node
        length = 0
        while fast.next:
            fast = fast.next
            length += 1
        if k % length == 0:
            return head
        fast = Node
        for _ in range(k % length):
            if fast.next:
                fast = fast.next
            else:
                fast = head
        slow = Node
        while fast.next:
            fast = fast.next
            slow = slow.next
        l1 = slow.next
        slow.next = None
        fast.next = head
        return l1



# @lc code=end

