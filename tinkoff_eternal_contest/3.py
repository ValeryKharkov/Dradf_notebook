n, t = map(int, input().split())
floors = list(map(int, input().split()))
x = int(input())

min_ = min(floors)
max_ = max(floors)
x = floors[x - 1]


if t < x:
    result_1 = (max_ - min_ + x - min_)
    result_2 = (max_ - min_ + max_ - x)
    result = min(result_1, result_2)
else:
    result = max_ - min_

print(result)