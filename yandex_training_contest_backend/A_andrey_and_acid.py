# Задача: Андрей и кислота
n = int(input("Кол-во резервуаров: "))
litre = map(int, input("Кол-во литров во всех резервуарах по порядку (ввод через пробел): ").split())

initial_volume = list(litre)

result = 0
max_litre = initial_volume[0]

for i in range(len(initial_volume)):
    max_litre = max(initial_volume[i], max_litre)
    if initial_volume[i] < max_litre:
        result = -1
        break

if result == 0:
    print(max(initial_volume) - min(initial_volume))
else:
    print(result)


