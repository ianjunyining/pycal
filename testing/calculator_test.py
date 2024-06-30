import unittest as ut
from src.calculator import Calculator
from src.complex import Complex

class Test_calculator(ut.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def compare_complex(self, complex, expect_real, expect_image):
        self.assertAlmostEqual(complex.real, expect_real)
        self.assertAlmostEqual(complex.image, expect_image)    

    def _test_expression(self):
        calculator = Calculator()
        result = calculator.calculate("4(-1)^3 + sin(i(1/2 + i^i))") # -4 + 0.768497554 i
        self.compare_complex(result, -4, 0.768497554)

    def _test_simple_expression(self):
        calculator = Calculator()
        result = calculator.calculate("3+-2")
        self.compare_complex(result, 1, 0)

    def _test_var(self):
        calculator = Calculator()
        calculator.calculate("d = 3")
        result = calculator.calculate("d")
        self.compare_complex(result, 3, 0)

    def test_function(self):
        calculator = Calculator()
        calculator.calculate("f(x) = 3 * x", True)
        result = calculator.calculate("f(3)")
        self.compare_complex(result, 9, 0)

    def test_nested_function(self):
        calculator = Calculator()
        calculator.calculate("f(x) = 3 * x + 1", True)
        calculator.calculate("h(x) = f(f(f(x))) + 1", True)
        result = calculator.calculate("h(3)")
        self.compare_complex(result, 95, 0)

if __name__ == '__main__':
    ut.main()