'''
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
'''

from random import randint as random

VARIANTS = [-100, 100]
ITEMS = [5, 15]

answer = 0
list_ = [random(*VARIANTS) for _ in range(random(*ITEMS))]
for i in list_:
    if i < 0 and answer == 0:
        answer = i
    elif i < 0 and i > answer:
        answer = i

if answer == 0:
    print(f'В списке {list_} \nнет отрицательных элементов')
else:
    print(f'В списке {list_} \nмаксимальный отрицательный элемент: {answer}')