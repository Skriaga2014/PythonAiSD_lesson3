'''
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны любому из чисел в диапазоне от 2 до 9.
'''

NUMS_OT = 2
NUMS_DO = 99
KRATN_OT = 2
KRATN_DO = 9

print(f'В диапазоне от {NUMS_OT} до {NUMS_DO}:')

for i in range(KRATN_OT, KRATN_DO+1):
    n = 0
    for j in range(NUMS_OT, NUMS_DO+1):
        if j % i == 0:
            n += 1
    print(f'количество чисел, кратных {i}: {n}')



