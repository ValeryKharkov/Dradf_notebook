"""
Четыре человека выстроились в очередь друг за другом. Определите, правда ли, что они стоят по росту (неважно,
в порядке неубывания или порядке невозрастания).
"""
# test_list = [5, 5, 5, 5, 5]
test_list = list(map(int, input().split()))

flag = 0
if test_list == sorted(test_list, reverse=True) or test_list == sorted(test_list, reverse=False):
    flag = 1


if flag:
    print('YES')
else:
    print('NO')