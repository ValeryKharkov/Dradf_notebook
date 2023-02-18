data = [2, 3, 1]


# def print_symbol(symbol):
#     if symbol > 0:
#         return '|'
#     else:
#         return ' '


# def print_string_roof(list_arg):
#     result_string = ''
#     for i in list_arg:
#         result_string += print_symbol(i)
#     print(result_string)


def print_string_floor(list_arg):
    result_string = ''
    max_num = max(list_arg)
    for i in list_arg:
        if i < max_num:
           result_string += '0'
        elif i == max_num:
            result_string += '#'
    print(result_string)

for i in range(max(data)):
    print_string_floor(data)
    #new_data = list(map(lambda x: x - 1, data))
    max_num = max(data)
    for item in data:
        if item == max_num:
            item = max_num - 1

print('finish')


