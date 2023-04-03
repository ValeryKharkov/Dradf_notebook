# Ввод данных
initial_dict = {}

len_initial_dict = int(input())
for i in range(len_initial_dict):
    key, value = input().split()
    initial_dict[key] = int(value)

A, B = input().split('-')


# Тестовый ввод данных
# initial_dict = {
#     'ZENIT': 75,
#     'SOCHI': 66,
#     'DINAMO': 63,
#     'CSKA': 60,
#     'KRASNODAR': 59,
#     'LOKOMOTIV': 40,
#     'AKHMAT': 40,
# }
#
# A = 'LOKOMOTIV'
# B = 'AKHMAT'


# initial_dict = {
#     'ARGENTINA': 5,
#     'JAMAICA': 0,
#
# }
#
# A = 'ARGENTINA'
# B = 'JAMAICA'

# Изменение значения словаря в зависимости от статуса команды А
def modification_dict(arg_dict: dict, arg_A: str, arg_B: str, result: str) -> dict:
    if result == 'win':
        A_point, B_point = 3, 0
    elif result == 'draw':
        A_point, B_point = 1, 1
    elif result == 'lose':
        A_point, B_point = 0, 3

    arg_dict[arg_A] = arg_dict[arg_A] + A_point
    arg_dict[arg_B] = arg_dict[arg_B] + B_point

    return arg_dict


# Сортировка словаря
def sorted_dict(arg_dict: dict) -> dict:
    sorted_tuple = sorted(arg_dict.items(), key=lambda kv: (-kv[1], kv[0]), reverse=False)
    return dict(sorted_tuple)


# Исход игры
status_list = ['win', 'draw', 'lose']

result_list = []

copy_dict = initial_dict.copy()

# Перебор разных исходов игры и сохранение ответов в список
for status in status_list:
    mod_dict = modification_dict(initial_dict, A, B, status)
    sort_dict = sorted_dict(mod_dict)


    # Возврат в словарь исходных значений
    initial_dict.clear()
    initial_dict = copy_dict.copy()

    # Определение индекса элемента
    result = list(sort_dict.keys()).index(A) + 1
    result_list.append(result)

# Вывод результата
print(*result_list)
