#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (51.76%)
# Likes:    780
# Dislikes: 0
# Total Accepted:    139.6K
# Total Submissions: 267.5K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        if n == 2:
            return self.merge2Lists(lists[0], lists[1])
        mid = n // 2
        return self.merge2Lists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))


    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        h1, h2, ans = l1, l2, head
        while h1 and h2:
            if h1.val >= h2.val:
                ans.next = ListNode(h2.val)
                ans = ans.next
                h2 = h2.next
            else:
                ans.next = ListNode(h1.val)
                ans = ans.next
                h1 = h1.next
        if h1:
            ans.next = h1
        if h2:
            ans.next = h2
        return head.next

# @lc code=end

