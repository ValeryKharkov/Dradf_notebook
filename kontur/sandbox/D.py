# D. Детская площадка

# Ввод данных
# n, m = map(int, input('n m: ').split())
# matrix = []
# for i in range(n):
#    matrix.append([input() for _ in range(m)])

# Тестовый ввод данных
table = (
    "**********\n"
    "*...*....*\n"
    "*...*....*\n"
    "**********\n"
         )
print(table)



# Формирование слоёв четырёхугольника из списков без "*"
rectangle_layers = []

for row in table.split():
    row_list = [items for items in row.split('*') if items]
    rectangle_layers.append(row_list)

print(rectangle_layers)

# Определение высоты и максимальной ширины четырёхугольника
temp_height = 0
temp_width = 0

max_height = 0
max_width = 0

for layer in rectangle_layers:  # для каждого слоя
    if layer:  # если слой не пустой
        temp_height += 1  # увеличить высоту четырёхугольника
        temp_width = len(max(layer))  # выявить ширину четырёхугольника
    else:
        if max_width < temp_width:
            max_width = temp_width

        if max_height < temp_height:
            max_height = temp_height

        temp_height = 0
        temp_width = 0

print(max_height, max_width)

# Вывод результата
result = max_height * max_width
print(result)