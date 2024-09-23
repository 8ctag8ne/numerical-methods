from Simple_Iteration import *
from Modified_Newton import *
from pretty import pretty_table

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

inp = input('''Лабораторна робота з чисельних методів студента групи ТТП-31 Яготіна Назарія.
Оберіть метод знаходження наближеного розв'язку:
1 - Модифікований метод Ньютона для рівняння x^3 - 5x^2 - 4x + 20 = 0
2 - Метод простої ітерації для рівняння x^3 - 8x^2 + 9x + 18 = 0
''')
while inp.isnumeric() == False or (int(inp) != 1 and int(inp) != 2):
    inp = input("Введіть ціле число з діапазону [1, 2]: ")

inp = int(inp)

if inp == 2:
    a = simple_get_a()
    b = simple_get_b()
else:
    a = newton_get_a()
    b = newton_get_b()

precision = input(f"Введіть бажану точність у діапазоні від 10^-12 до {(b-a)/2}: ")
while is_float(precision) == False or float(precision) > (b-a)/2 or float(precision) < 1e-12:
    precision = input(f"Введіть бажану точність у діапазоні від 10^-12 до {(b-a)/2}: ")
precision = float(precision)


if inp == 2:
    iterations, x, f_x = simple_find_answer(precision)
    iterations.insert(0, "n")
    x.insert(0, "x_n")
    f_x.insert(0, "x_n - phi(x_n)")
    print(pretty_table(iterations, x, f_x))
    print("Апріорна оцінка:", simple_theoretical_iterations(precision))
    print("Апостеріорна оцінка:", iterations[-1])
elif inp == 1:
    iterations, x, f_x = newton_find_answer(precision)
    iterations.insert(0, "n")
    x.insert(0, "x_n")
    f_x.insert(0, "f(x_n)")
    print(pretty_table(iterations, x, f_x))
    # print("Апріорна оцінка:", simple_theoretical_iterations(precision))
    print("Апостеріорна оцінка:", iterations[-1])