# A. Индусская математика
source_string = '6174'
my_list = list(source_string)

M = sorted(my_list, reverse=True)
m = sorted(my_list)


def list_transform_int(num_list: list):
    s = ''.join(num_list)
    s = int(s)
    return s


K = list_transform_int(M) - list_transform_int(m)
print(K)
