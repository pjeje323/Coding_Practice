# -*- coding: utf-8 -*-

# 2016-11-21

#  Find the Difference!

# Given two strings s and t which consist of only lowercase letters.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Find the letter that was added in t.

# EX) input : s = "abcd", t = "abcde" / output : e

#-------------------------------------------------

def Find_the_difference(a, b):
    dif_list = []
    for i in a:
        if i in b:
            pass
        else:
            dif_list.append(i)
    for j in b:
        if j in a:
            pass
        else:
            dif_list.append(j)
    return dif_list

a = 'qwerty'
b = 'qertyu'

print Find_the_difference(a, b)

#-------------------------------------------------

# 양 쪽을 다 봐줘야 하므로 for문이 반대로 도는데, 비효율적인듯...
# 다른 더 좋은 방법은 없을까
