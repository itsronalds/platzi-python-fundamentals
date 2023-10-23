name = 'Ronald'
print(type(name))

# Changin the type of a variable to int
name = 25
print(type(name))

# Changing the type of a variable to boolean
name = True
print(type(name))

# String concatenation
print('Ronald' + ' Abu Saleh')

# Int addition
print(10 + 20)

# Concatenation error between string and int

# ❌ This throw an error because we are trying to concatenate a string with an int
# print('Ronald' + 25)

# ✅ This is correct because we are concatenating a string with a string
print('Ronald' + '25')

# Concatenation between string and int using transformation
name = 'Ronald'
age = 25

# ✅ This is correct because we are concatenating a string with a string
print('Hi, my name is ' + name + ' and I am ' + str(age) + ' years old')

# ✅ Best way to concatenate string and int is using the format function
print(f'Hi, my name is {name} and I am {age} years old')

# The input function always returns a string
age = input('How old are you? ==> ')
print(f'Your age in ten years will be {int(age) + 10}')
