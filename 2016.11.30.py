# -*- coding: utf-8 -*-

# 2016-11-30

# prime_number


def prime_number(x):
    result = []
    candidates = range(3, x)
    base = 2
    product = base

    while candidates:
        while product < x:
            if product in candidates:
                candidates.remove(product)
            product = product+base
        result.append(base)
        base = candidates[0]
        product = base
        del candidates[0]
    result.append(base)
    return result

print prime_number(10)
print prime_number(100)
print prime_number(1000)

# -------------------------------------------------
# 에라토스테네스의 체! 간단한듯 아닌듯 엄청난 코드!
# 다시 한 번 복습하기 위해 데려왔는데, 신기하다.
# 정말 코딩은 해도해도 어렵네...

# P.S. 들여쓰기 진짜진짜 중요하니 조심!!
