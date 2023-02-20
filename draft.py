stack = [4]
command = 'pop'
result = [1, 2, 3]

if command == 'pop':
    try:
        stack[-1]
    except IndexError:
        result.append('error')
    else:
        result.append(stack[-1])
        stack.pop()

print(result)
print(stack)
# try:
#     print(1 / int(input('Enter: ')))
# except ZeroDivisionError:
#     print("Ошибка деления на ноль.")
# except ValueError:
#     print("Невозможно преобразовать строку в число.")
# except Exception:
#     print("Неизвестная ошибка.")
# else:
#     print("Операция выполнена успешно.")
# finally:
#     print("Программа завершена.")



'''
try:
    <код , который может вызвать исключения при выполнении>
except <классисключения_1>:
    <код обработки исключения>
except <классисключения_2>:
    <код обработки исключения>
...
else:
    <код выполняется, если не вызвано исключение в блоке try>
finally:
    <код , который выполняется всегда>
    '''