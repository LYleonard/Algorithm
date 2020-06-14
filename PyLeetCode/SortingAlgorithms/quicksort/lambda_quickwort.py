#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'LYLeonard'
__mtime__ = '2018/4/13'
# Code Description: 使用python的lambda表达式（匿名函数）实现快速排序
"""
import random

'''
匿名函数，一行代码实现快速排序
'''
quick_sort = lambda array: array if len(array) <= 1 else \
    quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + \
    quick_sort([item for item in array[1:] if item > array[0]])


def random_sqe(n):
    '''
    随机生成测试用例
    :param n:
    :return: return a list of n size
    '''
    L = []
    for i in range(n):
        L.append(random.randint(0, 2*n))
    return L

n = 10
L = random_sqe(n)
print L
print quick_sort(L)