import numpy as np

import power_method
import jacobi_rotation
import newton_method
def print_info():
    print('''Лабораторна робота №3 з чисельних методів студента групи ТТП-31 Яготіна Назарія.
Оберіть задачу:
1.Зайти найменше власне значення матриці степеневим методом:
    3 1 1 0 
    1 3 0 2 
    1 0 4 1 
    0 2 1 4
2. Знайти наближення до всіх власних значень матриці методом обертань Якобі:
    3 1 1 0 
    1 3 0 2 
    1 0 4 1 
    0 2 1 4
3. Розв’язати систему нелінійних рівнянь методом Ньютона:
    x = e^{-y}
    y = e^x.
''')

matrix = [
            [3.0, 1.0, 1.0, 0.0],
            [1.0, 3.0, 0.0, 2.0],
            [1.0, 0.0, 4.0, 1.0],
            [0.0, 2.0, 1.0, 4.0]
          ]
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
    power_method.solve(np.array(matrix), 0.001)
elif inp == 2:
    jacobi_rotation.solve(5, matrix)
else:
    newton_method.solve(5, np.array([1, 1]))