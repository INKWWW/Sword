#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def Fibonacci(self, n):
        if n > 39:
            return
        else:
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                var0 = 0
                var1 = 1
                for i in xrange(2, n+1):
                    res = var0 + var1
                    var0 = var1
                    var1 = res
                return res