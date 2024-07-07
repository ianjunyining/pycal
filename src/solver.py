import math
from src.tree import Node
from src.term import TermType
from src.complex import Complex

class Solver():
    def __init__(self, calculator) -> None:
        self.calculator = calculator
        self.err = 1e-5
        self.max_irr = 1000
        self.h = Complex(real=1e-6)

    def solve(self,exp_tree: Node , x0):
        # point to num
        exp_tree.left[0].data.term_type = TermType.Operand
        x_last = Complex(real=math.inf)
        x_current = x0
        irr = 0
        while not x_current.comp(x_last, self.err) and irr < self.max_irr:
            irr += 1
            x_last = x_current
            p1 = self.evaluate(exp_tree, x_last)
            p2 = self.derivative_by_numeric(exp_tree, x_last)
            x_current = x_last.sub(p1.div(p2))
        return str(x_current)

    def evaluate(self, exp_tree:Node, val):
        # replace a number in function with val
        exp_tree.left[0].data.num = val
        return self.calculator.calculate_from_exp_tree(exp_tree)

    def derivative_by_numeric(self, exp_tree:Node, val):
        p1 = self.evaluate(exp_tree, val.add(self.h))
        p2 = self.evaluate(exp_tree, val)
        return p1.sub(p2).div(self.h)
        