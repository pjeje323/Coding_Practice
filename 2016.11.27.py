# -*- coding: utf-8 -*-

# 2016-11-27

# Power of Four
# Given an integer (signed 32 bits),
# write a function to check whether it is a power of 4.
# Given num = 16, return true. Given num = 5, return false.

# Use recursion!

# -------------------------------------------------
def Power_of_four(x):
    power_of_four_lst = []
    for i in range(1, 33):
        power_of_four_lst.append(4 ** i)

    if power_of_four_lst.count(x) == True:
        return True
    else:
        return False

# -------------------------------------------------

# Algorithm 공부를 거의 매일 진행하고 있는데,
# 긍정적인 방향으로 나아가고 있는 것인지.
# 제자리에서 맴돌고 있는 것인지에 대해 조금 더 생각해보자!
