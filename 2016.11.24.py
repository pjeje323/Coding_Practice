# -*- coding: utf-8 -*-

# 2016-11-24

# Ransom Note
# Given an arbitrary ransom note string and another string
# containing letters from all the magazines,
# write a function that will return true
# if the ransom note can be constructed from the magazines ;
# otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

import re

def Ransom_note(a , b):
    if re.search(a, b):
        return True
    else:
        return False


print Ransom_note('a', 'ab')
print Ransom_note('a', 'bbb')
