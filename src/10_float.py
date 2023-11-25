x = 3.3
y = 1.1 + 2.2

print(x)
print(y)

# ❌ False
print(x == y)

'''
Make comparisons with floating point numbers
'''

# As string method
y_str = format(y, '.2g')
print('str =>', y_str)

print(y_str == str(x))

# Using round method
y_round = round(y, 1)
print('round =>', y_round)

# Mathematic method
tolerance = 0.00001
print(abs(x - y) < tolerance)
