#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by LYleonard on 2020/5/25
# Describe: Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = start = 0
        dicts = {}
        for index,value in enumerate(s):
            if value in dicts:
                sum = dicts[value] + 1
                if sum > start:
                    start = sum
            num = index - start + 1
            if num > ans:
                ans = num
            dicts[value] = index
        return ans
