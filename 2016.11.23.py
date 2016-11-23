# -*- coding: utf-8 -*-

# 2016-11-22

#258. Add Digits
# Given a non-negative integer num, repeatedly add all its digits
# until the result has only one digit.

# For example:

# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2.
# Since 2 has only one digit, return it.

# -----------------------------------------------------------------

def Add_digits(x):
    digits = []
    for i in str(x):
        digits.append(int(i))

    return sum(digits)


a = 1234
b = 3
c = 8792836491872052793874
print Add_digits(a), Add_digits(b), Add_digits(c)

# 10 3 119

# -----------------------------------------------------------------

# for 문 없이 할 수 있는 방법은 뭘까...
