# H. Метро
a = int(input())
b = int(input())
n = int(input())
m = int(input())

min_a = a * (n - 1) + n
min_b = b * (m - 1) + m
max_a = a * (n - 1) + n + 2 * a
max_b = b * (m - 1) + m + 2 * b

t_min = max(min_a, min_b)
t_max = min(max_a, max_b)

if t_max < t_min:
    print(-1)
else:
    print(t_min, t_max)