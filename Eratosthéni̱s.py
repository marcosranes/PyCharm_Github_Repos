from time import sleep
Sum = Cont = 0
Num = int(input('Enter a Number: '))
print()
for i in range(1, Num + 1):
    if (i != 1 and i % 2 != 0 or 2 == i) and (i % 3 != 0 or 3 == i) and (i % 5 != 0 or 5 == i) and (i % 7 != 0 or 7 == i):
        Cont += 1
        Sum += i
        print('\033[32;1m', end='')
    else:
        print('\033[m', end='')
    if i % 10 == 0:
        print(f'{i:>3}')
        sleep(.5)
    else:
        print(f'{i:>3}', end='  ')
print('\n')
print(f'Legend: \033[32;1mPrime Numbers\033[m')
print(f'Countage: {Cont}')
print(f'Sum between numbers: {Sum}')
print('\n')
for i in range(1, Num + 1):
    if (i != 1 and i % 2 != 0 or 2 == i) and (i % 3 != 0 or 3 == i) and (i % 5 != 0 or 5 == i) and (i % 7 != 0 or 7 == i):
        print(f'{i}', end=' ')
