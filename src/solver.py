import math
from src.tree import Node
from src.term import TermType
from src.complex import Complex, unique_complex

class Solver():
    def __init__(self, calculator, log=False) -> None:
        self.calculator = calculator
        self.err = 1e-7
        self.max_irr = 1000
        self.h = Complex(real=1e-6)
        self.log = log

    def solve(self, exp_tree:Node):
        x0_list = [
            Complex(real=1, image=0),
            Complex(real=1, image=1),
            Complex(real=1, image=-1),
            Complex(real=-1, image=0),
            Complex(real=-1, image=1),
            Complex(real=-1, image=-1),
            Complex(real=0, image=1),
            Complex(real=0, image=-1),
        ]
        solutions = []
        for i in range(len(x0_list)):
            if self.log:
                print(f"try {i}-th initial x0: {x0_list[i]}")
            solutions.append(self._solve(exp_tree, x0_list[i]))

        valid_sol = []
        for solution in solutions:
            val = self.evaluate(exp_tree, solution)
            if val.almost_equal(Complex(real=0, image=0), self.err):
                valid_sol.append(solution)

        return unique_complex(valid_sol)
    
    def _solve(self,exp_tree: Node , x0):
        # point to num
        exp_tree.left[0].data.term_type = TermType.Operand
        x_last = Complex(real=math.inf)
        x_current = x0
        irr = 0
        while not x_current.almost_equal(x_last, self.err) and irr < self.max_irr:
            if self.log:
                print(f"it={irr}, current={x_current}")
            irr += 1
            x_last = x_current
            p1 = self.evaluate(exp_tree, x_last)
            p2 = self.derivative_by_numeric(exp_tree, x_last)
            x_current = x_last.sub(p1.div(p2))

        if self.log:
            print()

        return x_current

    def evaluate(self, exp_tree:Node, val):
        # replace a number in function with val
        exp_tree.left[0].data.num = val
        return self.calculator.calculate_from_exp_tree(exp_tree)

    def derivative_by_numeric(self, exp_tree:Node, val):
        p1 = self.evaluate(exp_tree, val.add(self.h))
        p2 = self.evaluate(exp_tree, val)
        return p1.sub(p2).div(self.h)
        