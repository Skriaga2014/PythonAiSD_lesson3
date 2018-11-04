'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''

from random import randint as random

VARIANTS = [1, 100]
ITEMS = [5, 15]
list_ = [random(*VARIANTS) for _ in range(random(*ITEMS))]

min_index1 = len(list_)-1
min_index2 = 0

for i in range(len(list_)):
    if list_[i] <= list_[min_index1]:
        min_index1 = i
    else:
       min_index2 = i

for i in range(len(list_)):
    if list_[i] < list_[min_index2] and i != min_index1:
        min_index2 = i

print('В списке', list_)
print(f'два минимальных значения: {list_[min_index1]} и {list_[min_index2]}')

