# -*- coding: utf-8 -*-

# 2016-11-26

# Happy number

# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process:
# Starting with any positive integer,
# replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.

# ex) 19 is a happy numbers


def happy_number(x):
    sum_num = []
    for i in range(len(str(x))):
        s1 =  int(str(x)[i])**2
        sum_num.append(s1)

    if sum(sum_num) == 1:
        print sum_num
        print "Happy number!"
    else:
        print sum_num
        happy_number(sum(sum_num))


x = 19
happy_number(x)

# ------------------------------------
# 재귀함수의 중요성!
