# 11. Стек с защитой от ошибок
stack = []
command = ''
result = []


def stack_model(stack: list, command: str, n:int=None):
    if command == 'push':
        stack.append(n)
        result.append('ok')

    elif command == 'pop':
        try:
            stack[-1]
        except IndexError:
            result.append('error')
        else:
            result.append(stack[-1])
            stack.pop()

    elif command == 'back':
        try:
            stack[-1]
        except IndexError:
            result.append('error')
        else:
            result.append(stack[-1])

    elif command == 'size':
        result.append(len(stack))

    elif command == 'clear':
        stack.clear()
        result.append('ok')

    elif command == 'exit':
        result.append('bye')
    return stack


while command != 'exit':
    input_data = input('Enter command: ').split()
    if len(input_data) == 2:
        command = input_data[0]
        n = input_data[1]
    elif len(input_data) == 1:
        command = input_data[0]
        n = None
    else:
        print('Неверный ввод данных')
    stack_model(stack, command, n)


for i in result:
    print(i)