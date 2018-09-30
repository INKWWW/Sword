#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_while():
    """test: which list can represent True / False"""
    l_1 = []
    l_2 = [1]
    l_3 = ['a']
    if l_1:
        print('l_1 represents true')
    if l_2:
        print('l_2 represents true')
    if l_3:
        print('l_3 represents true')


if __name__ == '__main__':
    test_while()