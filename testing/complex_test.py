import unittest as ut
from src.complex import Complex


class TestComplex(ut.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def compare_complex(self, complex, expect_real, expect_image):
        self.assertAlmostEqual(complex.real, expect_real)
        self.assertAlmostEqual(complex.image, expect_image)

    def test_pow(self):
        "(1 + i)^(2 + i) = -0.309743505 + 0.857658013 i"
        c1 = Complex(real=1, image=1)
        c2 = Complex(real=2, image=1)
        power = c1.pow(c2)
        print(power)
        self.compare_complex(power, -0.309743505, 0.857658013)

    def test_pow_big(self):
        "(-239829329823)^3"
        c1 = Complex(real=-239829329823, image=0)
        c2 = Complex(real=3, image=0)
        power = c1.pow(c2)
        print(power)
        self.compare_complex(power, -13794529160825774685277673333164767, 0)

    def test_div(self):
        c1 = Complex(real=1, image=1)
        c2 = Complex(real=2, image=1)
        div = c1.div(c2)
        self.compare_complex(div, 0.6, 0.2)
    
    def test_sin(self):
        c = Complex(real=1, image=1)
        sin = c.sin()
        # sin(1 + i) = 1.29845758 + 0.634963915 i
        self.compare_complex(sin, 1.29845758, 0.634963915)

    def test_cos(self):
        c = Complex(real=1, image=1)
        cos = c.cos()
        # sin(1 + i) = 1.29845758 + 0.634963915 i
        self.compare_complex(cos, 0.833730025, -0.988897706)
    
    def test_ln(self):
        c = Complex(real=1, image=1)
        ln = c.ln()
        self.compare_complex(ln, 0.34657359, 0.785398163)

    def test_tan(self):
        c = Complex(real=1, image=1)
        tan = c.tan()
        self.compare_complex(tan, 0.271752585, 1.08392333)

if __name__ == '__main__':
    ut.main()
    
        