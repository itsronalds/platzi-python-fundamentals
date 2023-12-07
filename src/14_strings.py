text = 'She know programming in Python'

# in operator
print('Python' in text)

if 'Python' in text:
    print('Python is in text')
else:
    print('Python is not in text')

# len method
size = len('I can programming in Python')
print(size)

# upper method
print(text.upper())

# loweb method
print(text.lower())

# count method
print(text.count('o'))

# swapcase method
print(text.swapcase())

# startswith method
print(text.startswith('She'))

# endwith method
print(text.endswith('thon'))

# replace method
print(text.replace('Python', 'Golang'))

# title
print(text.title())

# isdigit
print(text.isdigit())
print('123'.isdigit())
