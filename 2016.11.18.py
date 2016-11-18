# -*- coding: utf-8 -*-

# 2016-11-18

# 1. 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

def print_stars(x):
    for i in range(1,x+1):
        print '*'*i


#print_stars(5)


# 2. 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

def print_stars_reverse(x):
    print '*'*x
    if x-1 == 0:
        return '*'
    else:
        print_stars_reverse(x-1)

#print_stars_reverse(5)

# 3. 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제(오른쪽 정렬)

def print_stars_reverse(x):
    a = '*'*x
    print '{0:>5}'.format(a)
    if x-1 == 0:
        return '*'
    else:
        print_stars_reverse(x-1)

print_stars_reverse(5)

# 4. 첫째 줄에는 별 2*N-1개, 둘째 줄에는 별 2*N-3개, ..., N번째 줄에는 별 1개를 찍는 문제(가운데 정렬)

def print_stars_middle(x):
    for i in range(1, x+1):
        a = 2*x - 2*i
        print '{0:^10}'.format('*' * a)

print_stars_middle(5)
