numbers = (1, 2, 3, 5)
strings = ('Ronald', 'José', 'Alfonso', 'Ronald')
print(numbers)
print('0 =>', numbers[0])
print(type(numbers))

print(strings)
print(type(strings))

# Find the index of an element
index_1 = strings.index('Ronald')
print('index_1 =>', strings[index_1])

# Count the number of times an element appears
count_1 = strings.count('Ronald')
print(f'Ronaldo appears {count_1} times')

# Convert a tuple to a list
numbers_list = list(numbers)
print(numbers_list)
print(type(numbers_list))

# Append an element to a list
numbers_list.append(6)
print(numbers_list)

# Modify an element of a list
numbers_list[0] = 0
print(numbers_list)

# List to tuple
numbers_tuple = tuple(numbers_list)
print(numbers_tuple)
