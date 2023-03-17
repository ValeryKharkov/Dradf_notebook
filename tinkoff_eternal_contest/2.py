# Ваня принес на кухню рулет, который он хочет разделить с коллегами...
n = int(input())
if n == 1:
    print(0)
else:
    result = 1
    while n / 2 > 1:
        n = n / 2
        result += 1

    print(result)