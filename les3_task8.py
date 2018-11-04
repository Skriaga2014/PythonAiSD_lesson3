'''
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
в ее последнюю ячейку. В конце следует вывести полученную матрицу.
'''

matrix = []
for i in range(4):
    matrix.append([])
    summ = 0
    for j in range(4):
        n = int(input(f'Введите элемент матрицы [{i}][{j}]: '))
        matrix[i].append(n)
        summ += n
    matrix[i].append(summ)

print('\nЗаполненная Вами матрица:')
for i in range(len(matrix)):
    print(matrix[i][:-1])

print('\nДополненная компьютером матрица:')
for i in range(len(matrix)):
    print(matrix[i])

