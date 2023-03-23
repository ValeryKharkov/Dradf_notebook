initial_dict = {
    'ZENIT': 65,
    'SOCHI': 56,
    'DINAMO': 53,
    'CSKA': 50,
    'KRASNODAR': 50,
    'LOKOMOTIV': 48,
    'AKHMAT': 41,
}

def sorted_dict(arg_dict: dict) -> dict:
    sorted_tuple = sorted(arg_dict.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_tuple)



print(sorted_dict(initial_dict))

# >>> d = {'b': 9, 'a': 3, 'c': 7}
# >>> sorted_tuple = sorted(d.items(), key=lambda x: x[1])
# >>> sorted_tuple
# # [('a', 3), ('c', 7), ('b', 9)]
# # преобразовываем обратно в словарь
# >>> dict(sorted_tuple)
# # {'a': 3, 'c': 7, 'b': 9}




