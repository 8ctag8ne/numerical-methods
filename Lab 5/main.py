import numpy as np

import Interpolation
import average_rectangles
import simpson
def print_info():
    print('''Лабораторна робота №5 з чисельних методів студента групи ТТП-31 Яготіна Назарія.
Оберіть задачу:
1. Побудувати квадратурну формулу інтерполяційного типу для наближеного інтегралу функції 3*x^8 - 2*x^5 +3*x^2 +1 за цілочисельними вузлами на проміжку [0..4].
2. Наближено оцінити інтеграл функції 3*x^8 - 2*x^5 +3*x^2 + 1 за допомогою формули середніх прямокутників.
3. Наближено оцінити інтеграл функції 3*x^8 - 2*x^5 +3*x^2 + 1 за допомогою формули Сімпсона.
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
    Interpolation.solve([0, 1, 2, 3, 4])
elif inp == 2:
    average_rectangles.solve(0, 4, 0.001)
else:
    simpson.solve(0, 4, 0.001)