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

# решение из гугла, которое прошло проверку

# n = int(input())  # 1 <= n <= 100 000 | Amount of tanks
# Volumes = list(map(int, input().split()))  # Volume of each tank
# answer = 0
# maximal = Volumes[0]
# for i in range(len(Volumes)):
#     maximal = max(Volumes[i], maximal)
#     if Volumes[i] < maximal:
#         answer = -1
#         break
# if answer == 0:
#     print(max(Volumes) - min(Volumes))
# else:
#     print('answer', answer)

#print(max(Volumes) - min(Volumes) if answer == 0 else answer)


