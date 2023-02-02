with open('input.txt') as f:
    print(f)
    numbers = f.read().split()
    a, b = map(int, numbers)
    sum_numbers = a + b

with open('output.txt', 'w') as f:
    f.write(str(sum_numbers))

