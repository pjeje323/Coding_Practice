# -*- coding: utf-8 -*-

# 2016-11-20

# 오늘의 문제
# Given an array of integers, every element appears twice except for one.
# Find that single one.

lst_nums = [3, 3, 5, 5, 7]
lst_els = ['a', 'a', 'b', 'b', 'c']

#--------------------------------------------------
# 한 개 짜리 찾는 함수 구현
def find_one(lst):
    for i in lst:
        if lst.count(i) == 2 :
            lst.remove(i)
            lst.remove(i)
    return lst

print find_one(lst_els)
print find_one(lst_nums)

#--------------------------------------------------
# 왠지 list comprehension과 lambda 쓰면 한 줄에 끝날 것 같은데..
# 더 고민해봐야겠다.
