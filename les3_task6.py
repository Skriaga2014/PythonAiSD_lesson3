'''
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
'''

from random import randint as random

VARIANTS = [1, 100]
ITEMS = [5, 15]
list_ = [random(*VARIANTS) for _ in range(random(*ITEMS))]
min = list_[0]
max = list_[0]

for i in list_:
    if i < min:
        min = i
    elif i > max:
        max = i

min_max = list_[list_.index(min)+1: list_.index(max)]
max_min = list_[list_.index(max)+1: list_.index(min)]

if min_max == []:
    list2 = max_min
else:
    list2 = min_max

if list2 == []:
    print(f'В списке {list_}\nмужду минимальным значением {min} и максимальным {max} элементов нет')
elif len(list2) == 1:
    print(f'В списке {list_}\nмужду минимальным значением {min} и максимальным {max}')
    print(f'располагается элемент {list2[0]}')
else:
    summ = 0
    for i in list2:
        summ += i
    print(f'В списке {list_}\nмужду минимальным значением {min} и максимальным {max}\nрасполагаются элементы {list2}')
    print(f'Их сумма: {summ}')

