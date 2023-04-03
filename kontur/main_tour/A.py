# A. Известный художник

# Тестовый ввод
# N = 6
# days_list = [1, 2, 1, 3, 1, 3]

# Ввод данных
N = int(input())



days_list = list(map(int, input().split()))

# Поиск самого высокого и низкого значений контрастности
max_contr = 0
min_contr = 0

for i in days_list:
    if i > max_contr:
        max_contr = i

for j in days_list:
    if j < max_contr:
        min_contr = j

# Поиск индекса самого высокого значения контрастности в списке дней
index_i = len(days_list) - 1 - days_list[::-1].index(max_contr)
index_j = days_list.index(min_contr)

# Поиск номера дня с самой высокой и низкой контрастностью
i = index_i + 1
j = index_j + 1

# Вывод результата
print(i, j)
