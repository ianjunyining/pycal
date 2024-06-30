# 1. Overview
We designed and implemented a Calculator in python. It supports common operators, pre-defined functions, variable making and modifing, and imaginary numbers. Your welcome to download and use it and contribute your code here.

# 2. Supported 
This calculator supports all kinds of different functions.
## Numbers, constants, and variables
This calculator supports real numbers and imaginary numbers, e.g., `2 + 3i`. It also supports constants `e`, `π` or `pi`. You can also create variables e.g., `a = 3`
## Operators
It supports operators: `+`, `-`, `÷`, `*`, `^`, `!`, `%`, and `()`

## functions
It supports pre-defined functions: 
``
    self.func_map = {
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
``
# 3. How to use it?
This calculator is straight-forward e.g.,
- `3 * 2`
- `(4 + 3) * 2`
- `sin(π/2)cos(2e)`
- `i^i`
- `e^(iπ)`
- `a = 3 * 2 ^ 2`
- `b = a/2`


# 4. Basic design
Our design is a modularized design. We have the following modulars. Modulars are in src folder

## Complex
The class `Complex` defines the complex numbers and with the functions.

## Tree
We need to define a tree because we need it create expression trees. We can visualize the tree by calling `tree.show()`

## Terms
This Module defines common operators, pre-defined functions, and attributes
## Calculator
### Parse string
### In-order to post-order
### Post-order to expression tree
### Calculate from expression tree
