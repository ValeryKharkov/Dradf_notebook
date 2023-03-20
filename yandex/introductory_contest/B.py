with open('input_B.txt') as f:
    print(f)
    numbers = f.read().split()
    a, b = map(int, numbers)
    sum_numbers = a + b

with open('output_B.txt', 'w') as f:
    f.write(str(sum_numbers))

