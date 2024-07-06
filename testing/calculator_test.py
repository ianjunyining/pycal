import unittest as ut
import src.calculator as cal
from src.calculator import Calculator
from src.complex import Complex

class Test_calculator(ut.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def compare_complex(self, complex, expect_real, expect_image):
        self.assertAlmostEqual(complex.real, expect_real)
        self.assertAlmostEqual(complex.image, expect_image)    

    def test_expression(self):
        calculator = Calculator()
        result = calculator.calculate("4(-1)^3 + sin(i(1/2 + i^i))") # -4 + 0.768497554 i
        self.compare_complex(result, -4, 0.768497554)

    def test_simple_expression(self):
        calculator = Calculator()
        result = calculator.calculate("3+-2")
        self.compare_complex(result, 1, 0)

    def test_var(self):
        calculator = Calculator()
        calculator.calculate("d = 3")
        result = calculator.calculate("d")
        self.compare_complex(result, 3, 0)

    def test_function(self):
        calculator = Calculator()
        calculator.calculate("f(x) = 3 * x")
        result = calculator.calculate("f(3)")
        self.compare_complex(result, 9, 0)

    def test_func_mod(self):
        calculator = Calculator()
        calculator.calculate("f(N1) = N1 % 2")
        result = calculator.calculate("f(3)")
        self.assertAlmostEqual(1, result)

    def test_nested_function(self):
        calculator = Calculator()
        calculator.calculate("f(x) = 3 * x + 1")
        calculator.calculate("h(x) = f(f(f(x))) + 1")
        result = calculator.calculate("h(3)")
        self.compare_complex(result, 95, 0)

    def test_ufunc_two_params(self):
        calculator = Calculator()
        calculator.calculate("f(x, y) = x + y")
        result = calculator.calculate("f(3, 5)")
        self.compare_complex(result, 8, 0)

    def test_ufunc_three_params(self):
        calculator = Calculator()
        calculator.calculate("f(x, y, z) = x + y + z")
        result = calculator.calculate("f(3, 5, 7)")
        self.compare_complex(result, 15, 0)

    def test_ufunc_no_comma(self):
        calculator = Calculator()
        calculator.calculate("f(x y) = x + y")
        result = calculator.calculate("f(3, 5)")
        self.compare_complex(result, 8, 0)

    def test_local_var_scope(self):
        calculator = Calculator()
        calculator.calculate("f(x) = x + 1")
        calculator.calculate("f(3)")
        self.assertRaises(cal.UnknownVarable, calculator.calculate, "x")

    def test_ufunc_missing_para(self):
        calculator = Calculator()
        calculator.calculate("f(x, y) = x + y")
        self.assertRaises(cal.MissingOperand, calculator.calculate, "1+2+f(3)")

    def test_ufunc_missing_left_par(self):
        calculator = Calculator()
        self.assertRaises(cal.MissingLeftPar, calculator.calculate, "(2 + 3) * 2) + 1")

    def test_ufunc_missing_right_par(self):
        calculator = Calculator()
        self.assertRaises(cal.MissingRightPar, calculator.calculate, "(2 * (2 + 3) + 1") #

if __name__ == '__main__':
    ut.main()