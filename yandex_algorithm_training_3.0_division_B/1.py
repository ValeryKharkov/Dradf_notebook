# 1. Гистограмма
source_string = 'Hello, world!'
source_list = list(source_string)
source_list_sorted = sorted(source_list)
print(source_list_sorted)

source_dict = {character: source_list_sorted.count(character) for character in source_list_sorted}
print(source_dict)






'''
data =  ['32', '22', '12', '32', '22', '12', '31', '21', '11']
dict((x, data.count(x)) for x in data)
'''