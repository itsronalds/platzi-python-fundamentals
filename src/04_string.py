name = 'Ronald'
lastname = 'Abu Saleh'

print(name, lastname)

# String concatenation
fullname = name + lastname
print(fullname)

# Put a space between the name and lastname
fullname = name + ' ' + lastname
print(fullname)

# Ways to use apostrophes in string
quote = "I'm a programmer"
print(quote)

quote = 'I\'m a programmer'
print(quote)

quote2 = 'My favorite language is "Python"'
print(quote2)

# Ways to format a string

# Way 1
template1 = 'Hi, my name is ' + name + ' and my lastname is ' + lastname
print(template1)

# Way 2
template2 = 'Hi, my fullname is {} and I\'m {} years old'.format(fullname, 25)
print(template2)

# Way 3
template3 = f'Hi, my fullname is {fullname} and I\'m {25} years old'
print(template3)
