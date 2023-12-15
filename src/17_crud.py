# CRUD Create, Read, Update & Delete

# Create
numbers = [1, 2, 3, 4, 5]

# Read
print(numbers[0])

# Update
numbers[0] = 0

# Delete
del numbers[0]

# Append
numbers.append(6)

# Insert
numbers.insert(0, 'Python')
print(numbers)

numbers.insert(1, 'Golang')
print(numbers)

# List union
tasks = ['Learn Python', 'Learn English']

new_list = numbers + tasks
print(new_list)

# Update list position
list_index = new_list.index('Python')
new_list[list_index] = 'Learn Angular'

print(new_list)

# Remove
new_list.remove(2)
new_list.remove(3)
print(new_list)

# Remove last element
new_list.pop()
print(new_list)

# Remove by index
new_list.pop(2)
print(new_list)

# Reverse
new_list.reverse()
print(new_list)

# Sort
numbers_a = [2, 1, 4, 3, 5]

# Ascending
numbers_a.sort()
print(numbers_a)

# Descending
numbers_a.sort(reverse=True)
print(numbers_a)

# Sort strings (alphabetically)
strings = ['Python', 'Golang', 'Javascript', 'Java']
strings.sort()
print(strings)

# Sort only works with the same data type
