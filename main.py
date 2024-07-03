from src.calculator import Calculator

def display_global_var(global_var:dict):
    for key, val in global_var.items():
        print(key, "=", str(val))

if __name__ == '__main__':
    calculator = Calculator()
    history = []
    while True:
        input_str = input("> ")
        if input_str == "q" or input_str == "quit":
            break
        elif input_str == "ls":
            history.append(input_str)
            display_global_var(calculator.global_vars)
        elif input_str == "h":
            print(history)
            history.append(input_str)
        elif input_str == "ch":
            history = []
            print("cleared history")
        else:
            try:
                history.append(input_str)
                result = calculator.calculate(input_str)
                if result == "q" or result == "quit":
                    break
                if result == "ls":
                    print()
                print(str(result))
            except Exception as e:
                print(e)
        