# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""从尾到头打印链表"""
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):  # listNode为该链表的头结点
        l = []
        node = listNode
        while node:
            l.insert(0, node.val)
            node = node.next
        return l       


if __name__ == '__main__':
    sol = Solution()
    l = sol.printListFromTailToHead([1,2,3])
    print(l)
