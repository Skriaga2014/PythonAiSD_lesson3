'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

from random import randint as random

VARIANTS = [-100, 100]
ITEMS = [2, 10]

list_ = [random(*VARIANTS) for _ in range(random(*ITEMS))]
max = list_[0]
min = list_[0]

for i in list_:
    if i > max:
        max = i
    if i < min:
        min = i

print(f'Оригинальный список: {list_}')
print(f'min = {min}')
print(f'max = {max}')
print(f'Меняем значения {min} и {max} местами:')
list_[list_.index(min)], list_[list_.index(max)] = list_[list_.index(max)], list_[list_.index(min)]

print(list_)