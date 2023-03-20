# B. Недостающее число

my_list = [10, -10, -10]

# my_list = []
# n = int(input())
# for i in range(n):
#     element = int(input())
#     my_list.append(element)


def remove_element(arg_list: list):
    for i in arg_list:
        arg_list.remove(i)
        arg_list.remove(-i)
        break
    return arg_list


while len(my_list) > 1:
    remove_element(my_list)

num = my_list[0]

if num < 0:
    response = abs(num)
else:
    response = -abs(num)

print(response)