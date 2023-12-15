numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['Make a coffee', 'Drink coffee', 'Go to sleep']
print(tasks)

types = [1, 2.0, True, 'Hello']
print(types)

# Accessing elements
print(numbers[0])
print(tasks[0])

# String is inmmutable
text = 'Hello Python!'
# ❌ text[0] = 'h'

# List is mutable
tasks[0] = 'Watch Platzi courses'
print(tasks)

# Slicing
print(tasks[0:2])

# In operator
print('Watch Platzi courses' in tasks)
