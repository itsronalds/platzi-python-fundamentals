'''
Arithmetic operators

Note: In Python the division operator / always returns a float value.
'''

print(10 + 10)
print(10 - 5)
print(10 * 2)
print(10 / 2)

# Inexact division return the remainder in this case return 1
print(10 % 3)

# Exact division return 0
print(10 % 2)

# Division with integer result

# This operator return always an integer value
print(10 // 3)

# Exponentiation
print(2 ** 3)

# Arithmetic operators in strings
print('Hello ' + 'World')
print('Hello World ' * 3)

'''
In Python the order of precedence is the same as in mathematics.

1. Parentheses
2. Exponentiation
3. Multiplication
4. Division
5. Addition
6. Subtraction
'''

print(2 ** 3 + 3 - 7 / 1 // 4)

print(2 ** 3)
print((7 / 1) // 4)

# The same expression but with parentheses
print(8 + 3 - 1)

# Python exception when we try to divide by zero

# ❌ ZeroDivisionError: division by zero
print(10 / 0)
