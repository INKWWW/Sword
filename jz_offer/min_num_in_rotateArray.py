#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0

        elif len(rotateArray) == 1:
            return rotateArray[0]

        else:
            val = rotateArray[0]
            for item in rotateArray:
                if item < val:
                    val = item
            return val