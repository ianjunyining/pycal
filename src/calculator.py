import math
import re
from src.tree import Node, Tree
from src.term import Term, TermType, FUNC, OP, TermAttr, UfuncAttr
from src.complex import Complex


class Calculator:
    def __init__(self) -> None:
        self.global_vars = {}
        self.local_vars = {}
        self.ufunc_map = {}
        self.expression = None

    def split_number_and_variable(self, input_str):
        # Define the regular expression pattern
        # replace "π" with "pi"
        pattern = r"([-+]?\d*\.?\d+)([ a-zA-Zπ]+)"
        
        # Use the re.match() function to find the match
        match = re.match(pattern, input_str)
        
        if match:
            # case 1 (num)(var)
            number = match.group(1)
            variable = match.group(2)
            return number, variable
        else:
            # case 2 (var)(var)
            pattern = r"([eiπ])[ ]*([eiπ])"
            match = re.match(pattern, input_str)
            if match:
                number = match.group(1)
                variable = match.group(2)
                return number, variable
        return None, None
        
    def modify_parts(self, parts):
        new_parts = []
        for part in parts:
            num, var = self.split_number_and_variable(part)
            if not num and not var or var == " ":
                new_parts.append(part)
            else:
                new_parts.append(num)
                new_parts.append('*')
                new_parts.append(var)
        return new_parts

    def parse_string(self, expression):
        terms = []
        pattern = r"([+\-*/^\(\)\!\%\,\=])"
        parts = re.split(pattern, expression)
        parts = [part.strip() for part in parts]
        parts = self.modify_parts(parts)
        parts = [part.strip() for part in parts]
        termattr = TermAttr
        op_map = termattr.op_map()
        func_map = termattr.func_map()
        for term in parts:
            if not term:
                continue
            if term[0].isnumeric():
                terms.append(Term(TermType.Operand, num=Complex(real=float(term))))
            elif term == "π" or term == "pi":
                terms.append(Term(TermType.Operand, num=Complex(real=float(math.pi))))
            elif term == "e":
                terms.append(Term(TermType.Operand, num=Complex(real=float(math.e))))
            elif term == "i":
                terms.append(Term(TermType.Operand, num=Complex(image=1)))
            elif term == "":
                pass
            elif term in func_map.keys():
                terms.append(Term(TermType.Func, func=func_map[term]))
            elif term in op_map.keys():
                terms.append(Term(TermType.Operator, op=op_map[term]))
            else:
                terms.append(Term(TermType.Var, var=term))
                    
        return terms

    def modify_in_order(self, terms):
        last_term = None
        new_terms = []
        for term in terms:
            if not last_term:
                if term.op == OP.SUB:
                    # -1 + 3
                    new_terms.append(Term(TermType.Operator, op=OP.NEG))
                else:
                    new_terms.append(term)
            else:
                if last_term.term_type == TermType.Operator and term.op == OP.SUB:
                    # 3 * -1
                    new_terms.append(Term(TermType.Operator, op=OP.NEG))
                elif last_term.op == OP.LEFT_PAR and term.op == OP.SUB:
                    # 3 (-1)
                    new_terms.append(Term(TermType.Operator, op=OP.NEG))
                elif last_term.term_type == TermType.Operand and \
                    (term.op == OP.LEFT_PAR or term.term_type == TermType.Func):
                    # 3 sin(i), 3(3+5)
                    new_terms.append(Term(TermType.Operator, op=OP.MUL))
                    new_terms.append(term)
                elif last_term.term_type == TermType.Operator and \
                    last_term.op == OP.RIGHT_PAR and term.term_type == TermType.Func:
                    # cos(1)sin(1)
                    new_terms.append(Term(TermType.Operator, op=OP.MUL))
                    new_terms.append(term)
                elif last_term.term_type == TermType.Var and term.term_type == TermType.Operator and term.op == OP.LEFT_PAR:
                    new_terms[-1] = Term(TermType.UFUNC, ufunc=last_term.var)
                    new_terms.append(term)
                else:
                    new_terms.append(term)
                

            last_term = term
        return new_terms


    def operation(self, num1:Complex, num2:Complex, op:OP):
        main_num = num2 if num1 == None else num1

        if op == OP.ADD:
            return num1.add(num2)
        elif op == OP.SUB:
            return num1.sub(num2)
        elif op == OP.MUL:
            return num1.mul(num2)
        elif op == OP.DIV:
            return num1.div(num2)
        elif op == OP.POW:
            return num1.pow(num2)
        elif op == OP.FAC:
            return math.gamma(main_num.real + 1)
        elif op == OP.MOD:
            return num1.real % num2.real
        elif op == OP.NEG:
            return main_num.neg()
    
    def func_call(self, num1:float, num2:float, func:FUNC):
        if func == FUNC.SIN:
            return num1.sin()
        elif func == FUNC.COS:
            return num1.cos()
        elif func == FUNC.LN:
            return num1.ln()
        elif func == FUNC.SQRT:
            return num1.pow(Complex(real=0.5))
        elif func == FUNC.EXP:
            e = Complex(real=math.e)
            return e.pow(num1)
        elif func == FUNC.TAN:
            return num1.tan()
        elif func == FUNC.ARCSIN:
            return num1.arcsin()
        elif func == FUNC.GCD:
            return math.gcd(int(num1.real), int(num2.real))
        elif func == FUNC.LCM:
            return math.lcm(int(num1.real), int(num2.real))
        elif func == FUNC.PERM:
            return math.perm(int(num1.real), int(num2.real))
        elif func == FUNC.COMB:
            return math.comb(int(num1.real), int(num2.real))
        elif func == FUNC.FLOOR:
            return math.floor(num1.real)
        elif func == FUNC.CEIL:
            return math.ceil(num1.real)
        elif func == FUNC.ABS:
            return math.fabs(num1.real)
        
    def ufunc_call(self, num, ufunc):
        ufunc_attr = self.ufunc_map[ufunc]
        self.local_vars[ufunc_attr.paramaters[0]] = num
        return self.calculate_from_exp_tree_no_assignment(ufunc_attr.exp_tree)

    def calculate_from_exp_tree_no_assignment(self, node: Node):
        if not node:
            return 
        if node.data.term_type == TermType.Operator:
            if TermAttr.op_operands(node.data.op) == 2:
                # First recur on left subtree
                num1 = self.calculate_from_exp_tree_no_assignment(node.left)

                # Then recur on right subtree
                num2 = self.calculate_from_exp_tree_no_assignment(node.right)
                return self.operation(num1, num2, node.data.op)
            else:
                num = self.calculate_from_exp_tree_no_assignment(node.right)
                return self.operation(num, 0, node.data.op)
        elif node.data.term_type == TermType.Func:
            if TermAttr.func_operands(node.data.func) == 2:
                num1 = self.calculate_from_exp_tree_no_assignment(node.left)
                num2 = self.calculate_from_exp_tree_no_assignment(node.right)
                return self.func_call(num1, num2, node.data.func)
            else:
                num = self.calculate_from_exp_tree_no_assignment(node.left)
                return self.func_call(num, 0, node.data.func)
        elif node.data.term_type == TermType.UFUNC:
            num = self.calculate_from_exp_tree_no_assignment(node.left)
            return self.ufunc_call(num, node.data.ufunc)
        elif node.data.term_type == TermType.Var:
            var = node.data.var
            if var in self.local_vars.keys():
                return self.local_vars[var]
            elif var in self.global_vars.keys():
                return self.global_vars[var]
            else:
                raise Exception(f"unknown variable: {var}")
        else:
            return node.data.num


    def calculate_from_exp_tree(self, node: Node):
        rterm = node.data
        if rterm.is_assignment():
            if node.left.data.term_type == TermType.UFUNC:
                paramater = [node.left.left.data.var]
                func_name = node.left.data.ufunc
                self.ufunc_map[func_name] = UfuncAttr(node.right, paramater, self.expression)
            else:
                var = node.left  
                num = self.calculate_from_exp_tree_no_assignment(node.right)
                self.global_vars[var.data.var] = num

        else:
            return self.calculate_from_exp_tree_no_assignment(node)

    def post_order_to_expression_tree(self, post_order_list):
        stack = []
        for item in post_order_list:
            if item.term_type == TermType.Operator:
                right = stack.pop()
                left = stack.pop() if TermAttr.op_operands(item.op) == 2 else None
                parent = Node(item)
                parent.left = left
                parent.right = right
                stack.append(parent)
            elif item.term_type == TermType.Func:
                right = stack.pop() if TermAttr.func_operands(item.func) == 2 else None
                left = stack.pop() 
                parent = Node(item)
                parent.left = left 
                parent.right = right
                stack.append(parent)
            elif item.term_type == TermType.UFUNC:
                left = stack.pop()
                parent = Node(item)
                parent.left = left 
                stack.append(parent)
            else:
                stack.append(Node(item))
        return stack[0]
    

    def in_order_to_post_order(self, terms : list):
        post_order = []
        stack = []
        for term in terms:
            if term.term_type == TermType.Operator or term.term_type == TermType.Func or \
                term.term_type == TermType.UFUNC:
                if term.op == OP.LEFT_PAR:
                    stack.append(term)
                elif term.op == OP.RIGHT_PAR:
                    while stack[-1].op != OP.LEFT_PAR:
                        if stack:
                            post_order.append(stack.pop())
                        else:
                            raise Exception("Missed right parentesis")
                    stack.pop()
                elif len(stack) == 0:
                    stack.append(term)
                else:
                    while stack and TermAttr.priority_not_less(stack[-1].op, term.op):
                        post_order.append(stack.pop())
                    stack.append(term)
            else:
                post_order.append(term)
        while stack:
            post_order.append(stack.pop())
        return post_order
    
    def calculate(self, expression: str, log=False):
        tree = Tree()
        self.expression = expression
        terms = self.parse_string(expression)
        new_terms = self.modify_in_order(terms)
        post_order = self.in_order_to_post_order(new_terms)
        expression_tree = self.post_order_to_expression_tree(post_order)
        result = self.calculate_from_exp_tree(expression_tree)
        if log:
            print([str(term) for term in terms])
            print([str(term) for term in new_terms])
            print([str(term) for term in post_order])
            tree.show(expression_tree, [])
        return result