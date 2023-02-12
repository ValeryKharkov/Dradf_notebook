# Задача: Посадка в самолет

seating = []  # рассадка по всем рядам
requirements = []  # список требований групп пассажиров

with open('input_B.txt', 'r') as file:
    n = int(file.readline().strip())  # ряд
    for i in range(n):
        seating.append(file.readline().strip())

    m = int(file.readline().strip())  # кол-во групп пассажиров
    for i in range(m):
        requirements.append((file.readline().strip()))

    for i in requirements:
        requirements_row = [num for num in i.split()]
        num = requirements_row[0]  # кол-во пассажиров
        side = requirements_row[1]  # сторона
        position = requirements_row[2]  # желаемое место

print(seating)
print(requirements)


def check_num(seating_arg, num_arg):
    # count_num = 0
    # for row in seating_arg:
    #     print('row:', row)
    #     for symbol in row:
    #         print('symbol: ', symbol)
    #
    #         if symbol == '.':
    #             count_num += 1
    # print(count_num)
    return num_arg * '.' in seating_arg

    # left = i[:3]
    # right = i[4:]
    # print(left, '<>', right)
    # for point in left:


def check_side(seating_arg, side_arg):
    if side_arg == 'left' and seating_arg.find('.', 0, 3) != -1:
        return True
    elif side_arg == 'right' and seating_arg.find('.', 4, 7) != -1:
        return True
    else:
        return False


def check_position(seating_arg, position_arg):
    if position_arg == 'window' and seating_arg[0] == '.' or seating_arg[-1] == '.':
        return True
    elif position_arg == 'aisle' and seating_arg[2] == '.' or seating_arg[4] == '.':
        return True
    else:
        return False


# def check_all_requirements(seating_arg, num_arg, side_arg, position_arg):
#     if check_num(seating_arg, num_arg) and
#     check_side(seating_arg, side_arg),
#     check_position(seating_arg, position_arg)


print(check_all_requirements('..._.#.', '2', 'left', 'aisle'))
