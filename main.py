from src.calculator import Calculator

help_str = """
Supported predefined functions
        return {
            "sin" : FUNC.SIN,
            "cos" : FUNC.COS,
            "ln" : FUNC.LN,
            "sqrt" : FUNC.SQRT,
            "exp" : FUNC.EXP,
            "tan" : FUNC.TAN,
            "gcd" : FUNC.GCD,
            "lcm" : FUNC.LCM,
            "p" : FUNC.PERM,
            "comb" : FUNC.COMB,
            "floor" : FUNC.FLOOR,
            "ceil" : FUNC.CEIL,
            "abs" : FUNC.ABS,
            "arcsin" : FUNC.ARCSIN,
            "asin" : FUNC.ARCSIN,
        }
Supported operators
        return {
            "+" : OP.ADD,
            "-" : OP.SUB,
            "*" : OP.MUL,
            "/" : OP.DIV,
            "^" : OP.POW,
            "(" : OP.LEFT_PAR,
            ")" : OP.RIGHT_PAR,
            "!" : OP.FAC,
            "%" : OP.MOD,
            "=" : OP.ASSIGNMENT,
        }

define user function e.g.,
f(x) = 3x + 1
g(y) = 2y + 1
rec(n) = n % 2
"""

def display_var_and_ufunc(global_var:dict, ufunc_map:dict):
    for key, val in global_var.items():
        print(key, "=", str(val))
    for key, val in ufunc_map.items():
        print(val.expression)
    

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
        else:
            try:
                result = calculator.calculate(input_str, log)
                print(str(result))
            except Exception as e:
                print(e)