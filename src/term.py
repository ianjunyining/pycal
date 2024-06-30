from enum import Enum
from src.complex import Complex

class OP(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    POW = 5
    LEFT_PAR = 6
    RIGHT_PAR = 7
    FUNC_OP = 8
    FAC = 9
    MOD = 10
    NEG = 11
    NONE = 12
    ASSIGNMENT = 15


class FUNC(Enum):
    SIN = 1
    COS = 2
    LN = 3
    SQRT = 4
    EXP = 5
    TAN = 6
    GCD = 7
    LCM = 8
    COMB = 9
    PERM = 10
    FLOOR = 11
    CEIL = 12
    ABS = 13
    ARCSIN = 14

class TermAttr:
    def priority_not_less(op1 : OP, op2 : OP):
        priority = {
            OP.ASSIGNMENT : 0,
            OP.LEFT_PAR : 1,
            OP.RIGHT_PAR : 1,
            OP.SUB : 2,
            OP.ADD : 2,
            OP.DIV : 3,
            OP.MUL : 3,
            OP.POW : 4,
            OP.FAC : 5,
            OP.NEG : 5,
            OP.FUNC_OP : 6,
        }
        return priority[op1] >= priority[op2]

    def func_operands(func: FUNC):
        func_operands_dict = {
            FUNC.SIN : 1,
            FUNC.COS : 1,
            FUNC.LN : 1,
            FUNC.SQRT : 1,
            FUNC.EXP : 1,
            FUNC.TAN : 1,
            FUNC.GCD : 2,
            FUNC.LCM : 2,
            FUNC.COMB : 2,
            FUNC.PERM : 2, 
            FUNC.FLOOR : 1,
            FUNC.CEIL : 1,
            FUNC.ABS : 1,
            FUNC.ARCSIN : 1,
        }
        return func_operands_dict[func]

    def op_operands(op: OP):
        num_operands_dict = {
            OP.LEFT_PAR : 0,
            OP.RIGHT_PAR : 0,
            OP.SUB : 2,
            OP.ADD : 2,
            OP.DIV : 2,
            OP.MUL : 2,
            OP.POW : 2,
            OP.MOD : 2,
            OP.FUNC_OP : 1,
            OP.FAC : 1,
            OP.NEG : 1,
            OP.ASSIGNMENT : 2, 
        }
        return num_operands_dict[op]
    
    def func_map():    
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
    
    def op_map():
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

class TermType(Enum):
    Operator = 1
    Operand = 2
    Func = 3
    Var = 4

class Term():
    def __init__(self, term_type: TermType, num:Complex=None, op:OP=None, func:FUNC=None, var=None) -> None:
        self.term_type = term_type
        self.num = num
        if term_type == TermType.Operator and not isinstance(op, OP):
            raise Exception(f"expected OP type: {op}")
        self.op = op
        self.func = func
        self.var = var
        if term_type == TermType.Func:
            self.op = OP.FUNC_OP
    
    def __str__(self) -> str:
        if self.term_type == TermType.Operator:
            return str(self.op)
        elif self.term_type == TermType.Operand:
            return str(self.num)
        elif self.term_type == TermType.Var:
            return self.var
        else:
            return str(self.func)