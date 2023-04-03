# B. Недостающее число

# Тестовый ввод данных
# init_list = [3, -2, 1, 2, 1, -1, -1]

# Ввод данных
# init_list = []
# n = int(input())
# for i in range(n):
#     element = int(input())
#     init_list.append(element)

# Альтернативный ввод данных
n = int(input())
init_list = [int(input()) for i in range(n)]


# Удаление элементов из списка
def del_elements(arg_list: list) -> list:
    i = 0
    while i < len(arg_list):
        try:
            i_opposite_num = arg_list.index(-arg_list[i], i + 1)  # определение индекса противоположного элемента (начиная со следующего)
            del arg_list[i_opposite_num]  # удаление противоположного числа
            del arg_list[i]  # удаление текущего элемента
        except ValueError:  # если нет противоположного элемента
            i += 1  # переходим к следующему элементу
    return arg_list


# Получение элемента без пары
element_from_init_list = del_elements(init_list)[0]

# Определение противоположного числа
if element_from_init_list < 0:
    result = abs(element_from_init_list)
else:
    result = -abs(element_from_init_list)

# Вывод результата
print(result)

