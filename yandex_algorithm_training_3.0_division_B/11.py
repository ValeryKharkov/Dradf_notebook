stack = []
command = ''


def stack_model(stack:list, command:str, n=None):
    if command == 'push':
        stack.append(n)
        print('ok')
    elif command == 'pop':
        print(stack[-1])
        stack.pop()
    elif command == 'back':
        print(stack[-1])
    elif command == 'size':
        print(len(stack))
    elif command == 'clear':
        stack.clear()
        print('ok')
    elif command == 'exit':
        print('bye')
    return stack



enter_command, n = str(input('command: ')), input('n: ')
while enter_command != 'exit':
    stack_model(stack, enter_command, n)



# back
# exit
