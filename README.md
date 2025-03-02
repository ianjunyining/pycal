# 1. Overview
We designed and implemented a Calculator in python. It supports common operators, pre-defined functions, variable making and modifing, and imaginary numbers. Your welcome to download and use it and contribute your code here. This software is by Ian Ning©

# 2. Supported 
This calculator supports all kinds of different functions.

## Numbers, constants, and variables
This calculator supports real numbers and imaginary numbers, e.g., `2 + 3i`. 

It also supports constants `e`, `π` or `pi`. You can also create variables e.g., `a = 3`

## Operators
It supports operators: `+`, `-`, `÷`, `*`, `^`, `!`, `%`, and `()`

## functions
It supports pre-defined functions: 

    sin, cos, ln, sqrt, exp, tan, gcd, lcm, p, 
    comb, floor, ceil, abs, arcsin, asin

## user functions
It supports function making e.g. `f(x) = 3x + 1`, 

It supports unlimited number of parameters
`f(a, b, c, d, e) = a + b + c + d + e`

## Solve equations
    f(x)=x^3 - 100 * x^2 + x - 100
    solve(f(x))
    solve(f)
    solve(x^3 - 100 * x^2 + x - 100)


Found roots

    100.0
    -0.0 + 1.0i
    -0.0 - 1.0i

## commands
commands: `ls`, `help` or `?`, `h`, `ch`, `quit`, `log`

- `ls`: list variables and user made functions
- `h` : history
- `ch` : clear history
- `log`: turn on/off log (display terms and expression tree)

others are self-explainatory

# 3. How to use it?
Warning: It will not be accurate after 2^53 because we use `float`.

This calculator is straight-forward e.g.,
- `3 * 2`
- `(4 + 3) * 2`
- `sin(π/2)cos(2e)`
- `i^i`
- `e^(iπ)`
- `a = 3 * 2 ^ 2`
- `b = a/2`
- `d(a) = a + a^2 + a^3`
- `f(x)=x^3 - 100 * x^2 + x - 100`
- `solve(f(x))`: find roots for `f(x)`
- `2 + 2(6 + 2) * i / 4`
- `s = 3 + i^i`
- `f(x) = i * x + sin(x + s) `
- `ls`
- `solve(f)`
- `solve(x^6 + sin(x) + 1)`


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
Parse string turns functions and numbers into terms e.g.,

    6^3 + 4(2+3*2) + sin(i^i) 
    ==> 
    ['6.0', 'OP.POW', '3.0', 'OP.ADD', '4.0', 'OP.LEFT_PAR', '2.0', 'OP.ADD', '3.0', 'OP.MUL', '2.0', 'OP.RIGHT_PAR', 'OP.ADD', 'FUNC.SIN', 'OP.LEFT_PAR', '1.0i', 'OP.POW', '1.0i', 'OP.RIGHT_PAR']`

### In-order to post-order
Inorder traversal is a depth-first search algorithm for a binary search tree that first traverses the left subtree, then the root, then traverses the right subtree. Post order is the contents of the left subtree are printed first, Right subtree, then root

In-order: `3 + 2 * 4`

Post-order: `3 2 4 * + `

### Post-order to expression tree
Since post order is a type of way to display a tree we can turn the post order into a tree.
Post-order: `3 2 4 * +`

Tree: 
- OP.ADD
- |--- 3.0
- |--- OP.MUL
- ••••|--- 2.0
- ••••|--- 4.0

### Calculate from expression tree
We calculate the result in inorder from expression tree

## Solver
We define solver to find roots of a equations when it is equal to zero.

    solve(x^2 + 1)

# License
See [License](https://github.com/ianjunyining/pycal/blob/main/LICENSE).