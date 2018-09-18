#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""两个栈实现列表/队列的push和pop。
   关键点在于：栈是FILO，列表/队列是FIFO。他们的push和pop规矩不一样。
   具体做法：stack1直接压入栈；出栈的时候判断stack2为空，则将stack1中元素全部倒入stack2中，stack2不为空则直接出栈
"""

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        
    def pop(self):
        # return xx 



