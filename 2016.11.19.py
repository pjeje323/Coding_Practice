# -*- coding: utf-8 -*-

# 2016-11-19

# 1차원의 점들이 주어졌을 때,
# 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
# (단 점들의 배열은 모두 정렬되어있다고 가정한다.)


s = [1, 3, 4, 8, 13, 17, 20]

def shortest_distance(points):
    pair_list = []
    distance = []
    for i in range(0,len(points)):
        for j in range(1, len(points)):
            if i < j:
                a = points[i],points[j]
                pair_list.append(a)
                dist = points[j] - points[i]
                distance.append(dist)
    idx = distance.index(min(distance))
    print pair_list[idx]

shortest_distance(s)

# for문을 두번이나 돌려야 하고
# list를 동시에 두 개 생성해서 index로 값을 찾아야해서
# 효율성이 떨어지는 함수... 많이 아쉽다.
