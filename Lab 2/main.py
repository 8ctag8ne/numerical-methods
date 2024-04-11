import numpy as np
from numpy.f2py.auxfuncs import throw_error

import init_info
from jacobi import solve_eq_jacobi
from simple_iteration import solve_eq_simple_iteration
import init_info as in_inf
from sqrt_method import solve_eq_sqrt_method

in_inf.print_info()
inp = ""
while True:
    try:
        inp = int(input("Введіть ціле число з діапазону [1, 3]: "))
        if 1 <= inp <= 3:
            break
        else:
            raise ValueError
    except ValueError:
        print("Некоректний ввід")

precision = 0.001
if inp == 1 or inp == 3:
    precision = input(f"Введіть бажану точність у діапазоні від 10^-12 до 1 або натисніть enter, щоби лишити стандартну точність 0.001: ")
    if precision == "":
        precision = 0.001
    while in_inf.is_float(precision) == False or float(precision) > 1 or float(precision) < 1e-12:
        precision = input(f"Введіть бажану точність у діапазоні від 10^-12 до 1 або натисніть enter, щоби лишити стандартну точність 0.001: ")
        if precision == "":
            precision = 0.001
            break
    precision = float(precision)


a = np.array(init_info.matrices_a[inp - 1])
b = np.array(init_info.matrices_b[inp - 1]).T
if inp == 1:
    solve_eq_simple_iteration(a, b, precision)
elif inp == 2:
    solve_eq_sqrt_method(a, b)
elif inp == 3:
    solve_eq_jacobi(a, b, precision)