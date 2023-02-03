# Андрей и кислота
n = int(input("Кол-во резервуаров: "))
a = map(int, input("Кол-во литров во всех резервуарах по порядку (ввод через пробел): ").split())

initial_vulume = list(a)
# min_a = min(initial_vulume)
# max_a = max(initial_vulume)
# set_ = len(set(initial_vulume))
# count_min_a = 0
# count_max_a = 0
#
# for i in initial_vulume:
#     if i == min_a:
#         count_min_a += 1
#     elif i == max_a:
#         count_max_a += 1
#
#
#
# if count_min_a + count_max_a != n or set_ == 1:
#     k = -1
# elif count_min_a + count_max_a == n:
#     k = max_a - min_a
#
# print(k)


result = 0
maximal = initial_vulume[0]
for i in range(len(initial_vulume)):
     maximal = max(initial_vulume[i], maximal)
     if initial_vulume[i] < maximal:
         answer = -1
         break
print(max(initial_vulume) - min(initial_vulume) if answer == 0 else answer)


