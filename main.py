import os
from src.calculator import Calculator

help_str = """
Supported predefined functions
    sin, cos, ln, sqrt, exp, tan, gcd, lcm, p, 
    comb, floor, ceil, abs, arcsin, asin

Supported operators
    +, -, *, /, ^, !, %, =, (, )

Support constants, complex numbers, and variables
    pi, e, i
    x = e^(i * pi) + 1

Examples
    a = 1+i
    sin(a)cos(pi) + 5 * (2 + a)

define user function e.g.,
    f(x) = 3x + 1
    g(x, y) = 2y + x^2
    rec(n) = n % 2

solve equations
    f(x)=x^3 - 100 * x^2 + x - 100
    solve(f(x))

commands
    - `ls`: list variables and user made functions
    - `h` : history
    - `ch` : clear history
    - `log`: turn on/off log (display terms and expression tree)

"""

def display_var_and_ufunc(global_var:dict, ufunc_map:dict):
    for key, val in global_var.items():
        print(key, "=", str(val))
    for key, val in ufunc_map.items():
        print(val.expression)
    
def print_result(result):
    if not result:
        return
    if isinstance(result, list):
        print("ans =")
        for item in result:
            print(str(item))
    else:
        print("ans =", str(result))

if __name__ == '__main__':
    calculator = Calculator()
    history = []
    log = False
    while True:
        input_str = input("> ")
        history.append(input_str)
        if input_str == "q" or input_str == "quit":
            break
        elif input_str == "ls":
            display_var_and_ufunc(calculator.global_vars, calculator.ufunc_map)
        elif input_str == "h":
            for item in history:
                print(item)
        elif input_str == "ch":
            history = []
            print("cleared history")
        elif input_str == "log":
            log = not log
        elif input_str == "help" or input_str == "?":
            print(help_str)
        elif input_str == "clear":
            os.system("clear")
        else:
            try:
                result = calculator.calculate(input_str, log)
                print_result(result)
            except Exception as e:
                print(e)