#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by LYleonard on 2020/6/14
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
                guard = dicts[value] + 1
                if guard > start:
                    start = guard
            tmp_ans = index - start + 1
            if tmp_ans > ans:
                ans = tmp_ans
            dicts[value] = index
        return ans
