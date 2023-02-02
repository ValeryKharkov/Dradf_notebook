with open('input_G.txt', 'r') as file:
    j = file.readline().strip()
    s = file.readline().strip()

count = 0
for letter in s:
    if letter in j:
        count += 1

with open('output_G.txt', 'w') as file:
    file.write(str(count))