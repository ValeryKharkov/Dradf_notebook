# A. Кондиционер

troom, tcond = map(int, input('troom, tcond: ').split())
mode = input('mode: ')

if troom == tcond:
    print(troom)
elif troom > tcond:
    if mode == 'freeze' or mode == 'auto':
        print(tcond)
    elif mode == 'heat' or mode == 'fan':
        print(troom)
elif troom < tcond:
    if mode == 'freeze' or mode == 'fan':
        print(troom)
    elif mode == 'heat' or mode == 'auto':
        print(tcond)

