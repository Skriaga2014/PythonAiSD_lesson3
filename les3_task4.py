'''
4. Определить, какое число в массиве встречается чаще всего.
'''

from random import randint as random

VARIANTS = [0, 5]
ITEMS = [10, 20]

answer = (0,0)
list_ = [random(*VARIANTS) for _ in range(random(*ITEMS))]
for i in list_:
    if list_.count(i) > answer[1]:
        answer = (i,list_.count(i))

print(f'В списке {list_} \nчаще встречается число {answer[0]} (встречается {answer[1]} раз(а))')