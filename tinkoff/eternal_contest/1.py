# Костя подключен к мобильному оператору «Мобайл»...
A, B, C, D = map(int, input().split())
if D - B <= 0:
    result = A
else:
    result = A + C * (D - B)

print(result)