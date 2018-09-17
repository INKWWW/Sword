#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def replaceSpace(self, s):
        s_new = s.replace(' ', '%20')
        return s_new


class Solution2:
    def replaceSpace(self, s):
        s_new = ''
        s_list = s.split(' ')
        l = len(s_list)
        for i in s_list:
            if s_list.index(i) != l-1:
                s_new = s_new + i + '%20'
            else:
                s_new = s_new + i
        return s_new



if __name__ == '__main__':

    # sol = Solution()
    # s_out = sol.replaceSpace('We are happy')
    # print(s_out)

    sol2 = Solution2()
    s_out2 = sol2.replaceSpace('We are happy')
    print(s_out2)

