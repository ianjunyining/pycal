import math

class Complex():
    def __init__(self, real:float=0, image:float=0) -> None:
        self.real = real
        self.image = image

    def is_pure_real(self):
        return self.image == 0

    def is_pure_image(self):
        return self.real == 0

    def almost_equal(self, other, err):
        comp1 = math.fabs(self.real - other.real) < err
        comp2 = math.fabs(self.image - other.image) < err
        return comp1 and comp2

    def add(self, other):
        return Complex(
            real=self.real + other.real, 
            image=self.image + other.image
        )
    
    def sub(self, other):
        return Complex(
            real=self.real - other.real, 
            image=self.image - other.image
        )
    
    def mul(self, other):
        return Complex(
            real=self.real * other.real - self.image * other.image, 
            image=self.real * other.image + self.image * other.real
        )
    
    def mul_scale(self, scale : float):
        return Complex(real=self.real * scale, image=self.image * scale)

    def conjugate(self):
        return Complex(real=self.real, image=-self.image)
    
    def mod_sq(self):
        return self.real ** 2 + self.image ** 2

    def div(self, other):
        if (not isinstance(other, Complex)) or other.is_pure_real():
            return Complex(
                real=self.real / other.real,
                image=self.image / other.real,
            )
        return self.mul(other.conjugate()).mul_scale(1/other.mod_sq())  
    
    def neg(self):
        return Complex(real=-self.real, image=-self.image)
    
    def pow(self, other):
        """(x + iy)^(a + ib) = (r e^(iw))^(a + ib)
        = r^(a+ib)*e^(iw * (a + ib))
        = r^a * r^(ib) * e^(iwa - wb)             # r^a = e^(a ln(r)),  r^(ib) = e^(ib*ln(r))
        = e^(a ln(r) - wb) * e^(i(b ln(r) + wa))
        ===>
        R = e^(a ln(r) - wb)
        W = b ln(r) + wa
        (x + iy)^(a + ib) = R cos(W) + i R sin(W)

        (1 + i)^(2 + i) = -0.309743505 + 0.857658013 i"""
        z = other if isinstance(other, Complex) else Complex(real=other)

        if self.is_pure_real() and z.is_pure_real():
            val = Complex(
                real=self.real ** z.real,
                image=0,
            )
            if isinstance(val.real, complex):
                return Complex(
                    real=val.real.real,
                    image=val.real.imag
                )
            else:
                return val
        
        w = math.atan2(self.image, self.real)
        r = (self.real ** 2 + self.image ** 2) ** 0.5
        R = math.exp(z.real * math.log(r) - w * z.image)
        W = z.image * math.log(r) + w * z.real
        return Complex(
            real=R * math.cos(W),
            image=R * math.sin(W),
        )
    
    def sin(self):
        """
        e^iw = cos(w) + i sin(w)                                                    (1)
        e^(-iw) = cos(-w) + i sin(-w) = cos(w) - i sin(w)                 (2)

        Add (1) and (2), we get
        cos(w) = (e^iw + e(-iw)) / 2

        (1) - (2), we get
        sin(w) = (e^iw - e^(-iw)) / 2i

        sin(1 + i) = 1.29845758 + 0.634963915 i
        cos(1 + i) = 0.833730025 - 0.988897706 i
        """
        if self.is_pure_real():
            return Complex(
                real=math.sin(self.real),
                image=0,
            )
        e = Complex(real=math.e)
        f1 = e.pow(self.mul(Complex(image=1)))
        f2 = e.pow(self.mul(Complex(image=-1)))
        return f1.sub(f2).div(Complex(image=2))
    
    def cos(self):
        """
        e^iw = cos(w) + i sin(w)                                                    (1)
        e^(-iw) = cos(-w) + i sin(-w) = cos(w) - i sin(w)                 (2)

        Add (1) and (2), we get
        cos(w) = (e^iw + e(-iw)) / 2

        (1) - (2), we get
        sin(w) = (e^iw - e^(-iw)) / 2i

        sin(1 + i) = 1.29845758 + 0.634963915 i
        cos(1 + i) = 0.833730025 - 0.988897706 i
        """
        if self.is_pure_real():
            return Complex(
                real=math.cos(self.real),
                image=0,
            )
        e = Complex(real=math.e)
        f1 = e.pow(self.mul(Complex(image=1)))
        f2 = e.pow(self.mul(Complex(image=-1)))
        return f1.add(f2).mul_scale(0.5)
    
    def ln(self):
        """
        log(a*b) = log(a) + log(b)
        log(x+iy) = log(r * e^iw) = log(r) + log(e^iw) = log(r) + iw
        """
        if self.is_pure_real():
            return Complex(
                real=math.log(self.real),
                image=0,
            )
        w = math.atan2(self.image, self.real)
        r = (self.real ** 2 + self.image ** 2) ** 0.5
        return Complex(real=math.log(r), image=w)
    
    def tan(self):
        """
        tanz = sinz / cosz
        """
        if self.is_pure_real():
            return Complex(
                real=math.tan(self.real),
                image=0,
            )
        return self.sin().div(self.cos())
    
    def arcsin(self):
        """
        arcsin(z) = -i ln(iz + (1 - z^2)^0.5)
        """
        if self.is_pure_real():
            return Complex(
                real=math.asin(self.real),
                image=0,
            )
        a = self.mul(Complex(image=1))
        one = Complex(real=1)
        b = one.sub(self.pow(2)).pow(0.5)
        c = Complex(image=-1).mul(a.add(b).ln())
        return c

    def arccos(self):
        pass

    def arctan(self):
        pass

    def sec(self):
        pass

    def cot(self):
        pass
    
    def __str__(self) -> str:
        r_str = str(round(self.real, 10))
        i_str = str(math.fabs(round(self.image, 10)))
        if self.image > 0 and self.real != 0:
            return f"{r_str} + {i_str}i"
        elif self.image < 0 and self.real == 0:
            return f"-{i_str}i"
        elif self.image < 0 and self.real != 0:
            return f"{r_str} - {i_str}i"
        elif self.image == 0 and self.real != 0:
            return r_str
        elif self.image != 0 and self.real == 0:
            return i_str + "i"
        elif self.image == 0 and self.real == 0:
            return "0"
        

def unique_complex(nums: list):
    unique = []
    
    for num in nums:
        is_unique = True
        for u in unique:
            if num.almost_equal(u, 1e-6):
                is_unique = False
                break
        if is_unique:
            unique.append(num)

    return unique