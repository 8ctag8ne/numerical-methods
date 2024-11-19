import numpy as np

import unknown_coefficient
import linear_spline
import cubic_spline
def print_info():
    print('''Лабораторна робота №4 з чисельних методів студента групи ТТП-31 Яготіна Назарія.
Оберіть задачу:
1. Побудувати степеневий поліном методом невизначених коефіцієнтів за п’ятьма вузлами для функції 3∗x^8−2∗x^5+3∗x^2+1 на проміжку [0..4].
2. Побудувати кубічний сплайн для попередньої задачі за точками х = 0, 2, 4. Доповнити систему рівнянь значенням справжньої похідної на краях.
3. Побудувати лінійний сплайн для першої задачі з відстанню між точками розбиття інтервалу, рівною 0.5.
''')

while True:
    try:
        inp = int(input("Введіть ціле число з діапазону [1, 3]: "))
        if 1 <= inp <= 3:
            break
        else:
            raise ValueError
    except ValueError:
        print("Некоректний ввід")

if inp == 1:
    unknown_coefficient.solve(0, 4, 4)
elif inp == 2:
    cubic_spline.solve([0, 2, 4])
else:
    linear_spline.solve([i/2 for i in range(9)])