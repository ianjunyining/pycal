import unittest as ut
from src.calculator import Calculator


class TestSolver(ut.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def compare_complex(self, complex, expect_real, expect_image):
        self.assertAlmostEqual(complex.real, expect_real)
        self.assertAlmostEqual(complex.image, expect_image)

    def test_equation1(self):
        calculator = Calculator()
        calculator.calculate("f(x) = x + 1")
        result = calculator.calculate("solve(f(x))")
        self.compare_complex(result[0], -1, 0)

    def test_equation2(self):
        calculator = Calculator()
        calculator.calculate("f(x) = x^2 + sin(x) - 1", True)
        result = calculator.calculate("solve(f(x))")
        self.compare_complex(result[1], -1.409624, 0)

if __name__ == '__main__':
    ut.main()