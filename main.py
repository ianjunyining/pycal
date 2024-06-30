from src.calculator import Calculator

if __name__ == '__main__':
    calculator = Calculator()
    while True:
        expression = input("> ")
        try:
            result = calculator.calculate(expression, True)
            print(str(result))
        except Exception as e:
            print(e)