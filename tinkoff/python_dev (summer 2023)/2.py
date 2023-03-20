'''
В некоторой компании есть n джунов-разработчиков и m сеньор-разработчиков. Чтобы код, который написал джун,
мог попасть в прод....
'''
n, m, k = map(int, input().split())
t = (n * k + m - 1) // m
print(t)

# решение: https://www.cyberforum.ru/java-beginners/thread3090486.html