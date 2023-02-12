# I. Узник замка Иф
total_list = []
for i in range(5):
    total_list.append(int(input()))

abc_list = total_list[:3]
de_list = total_list[3:]


def remove_max(list_arg):
    list_arg.remove(max(list_arg))
    return list_arg


def perimeter(list_arg):
    sum_ = 0
    for num in list_arg:
        sum_ += num
    return sum_


hole_size = perimeter(de_list)
brick_size = perimeter(remove_max((abc_list)))


if max(abc_list) > max(de_list) or hole_size < brick_size:
    print('NO')
else:
    print('YES')
