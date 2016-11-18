# -*- coding: utf-8 -*-

# 2016-11-18
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

def print_stars(x):
    for i in range(1,x+1):
        print '*'*i


print_stars(5)
