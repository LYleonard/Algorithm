#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'LYLeonard'
__mtime__ = '2018/4/9'
# Code Description: 递归思想实现快速排序
"""
import time
import random

def quickSort(L):
    '''
    快速排序（分治思想），需要两个额外空间
    :param L:
    :return: 返回排好序的列表
    '''
    if len(L)<=1:
        return L
    Lleft = []
    Lright = []
    key = L[0]
    for i in L[1:]:
        if key < i:
            Lright.append(i)
        else:
            Lleft.append(i)
    return quickSort(Lleft) + [L[0]] +  quickSort(Lright)

###############################################################
def partitionHoareModify(arr, start, end):
    '''
    快速排序的划分函数
    :param arr:
    :param start:
    :param end:
    :return: 返回参考值的位置，该位置之前都比"哨兵"(pivot element)小，右边都比哨兵大
    '''
    cursorLeft = start-1 #set cursor for the left value
    cursorRight = end+1  #set cursor for the right value
    key = arr[start]  # set key value as standard
    while(True):
        while(True):
            cursorLeft += 1
            if (arr[cursorLeft] >= key):
                break
        while(True):
            cursorRight -=1
            if (arr[cursorRight] <= key):
                break
        if(cursorLeft < cursorRight):
            #swap the values
            temp = arr[cursorLeft]
            arr[cursorLeft] = arr[cursorRight]
            arr[cursorRight] = temp
        else:
            return cursorRight

def quicksort(arr, start, end):
    '''
    《算法导论》快速排序, 随机顺序平均时间复杂度nlogn，对于有序序列最坏时间复杂度为n^2.
    :param arr:
    :param start:
    :param end:
    :return: 对arr就地排序，无返回值
    '''
    if(start < end):
        position = partitionHoareModify(arr,start,end) #use partitionHoare is error because of do...while
        quicksort(arr,start,position)
        quicksort(arr,position+1,end)

########################################################
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

# L = [2,8,7,1,3,5,6,4]
# L1 = [6,8,7,10,3,20,9,4]
L = [1,8,15,11,8,3,2,6,4]

# n = 10000
# L = random_sqe(n)
t0 = time.time()
LL = quicksort(L, 0, len(L)-1)
t1 = time.time()
print t1-t0
print L

# L2 = random_sqe(n)
# t2 = time.time()
# LL = quickSort(L2)
# t3 = time.time()
# print t3-t2
#print LL