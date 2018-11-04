'''
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

from random import randint as random

VARIANTS = [1, 100]
ITEMS = [5, 10]

matrix = []
itm = [random(*ITEMS),random(*ITEMS)]

for i in range(itm[1]):
    matrix.append([random(*VARIANTS) for _ in range(itm[0])])

print(f'Матрица {itm[0]}*{itm[1]}:')
for i in range(len(matrix)):
    print(matrix[i])

answer = [0,0]
for i in range(itm[0]):
    min_column = matrix[0][i]
    for j in range(itm[1]):
        if matrix[j][i] < min_column:
            min_column = matrix[j][i]
    print(f'Минимальное число в {i+1}-м столбце: {min_column}')
    if min_column > answer[0]:
        answer = [min_column,i]

print(f'Максимальное число из них - {answer[0]} (находится в {answer[1]+1}-м столбце)')