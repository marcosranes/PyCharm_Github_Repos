from math import sqrt
Value = int(input('Enter Value [Max 120]: ')) # until 120
Numbers = list()
M2 = []  # multiples of 2
M3 = []  # multiples of 3
M5 = []  # multiples of 5
M7 = []  # multiples of 7
Multiples = []
Primes = []
print(f'Square Root of {Value} = {sqrt(Value)}')
for i in range(2, int(sqrt(Value)) + 1):
    Multiples.append(i)
    if i % 2 == 0 and 2 != i or i % 3 == 0 and 3 != i or i % 5 == 0 and 5 != i or i % 7 == 0 and 7 != i:
        Multiples.remove(i)
for i in range(1, Value + 1):
    Numbers.append(i)
    Primes.append(i)
    if i % 2 == 0:
        M2.append(i)
    if i % 3 == 0:
        M3.append(i)
    if i % 5 == 0:
        M5.append(i)
    if i % 7 == 0:
        M7.append(i)
    if i == 1 or i % 2 == 0 and 2 != i or i % 3 == 0 and 3 != i or i % 5 == 0 and 5 != i or i % 7 == 0 and 7 != i:
        Primes.remove(i)
print(f'So, just eliminate multiples of {Multiples}')
print(f'Numbers: {Numbers}')
print(f'M2 out: {M2}')
print(f'M3 out: {M3}')
print(f'M5 out: {M5}')
print(f'M7 out: {M7}')
print(f'Prime Numbers: {Primes}')
