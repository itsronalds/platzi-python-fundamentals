person = {
    'name': 'Ronald Abu Saleh',
    'age': 25,
    'ocupation': 'Software Engineer',
    'languages': ['Python', 'JavaScript', 'Java', 'PHP'],
}

print(person)

# Updating values
person['name'] = 'Ronald A. Saleh'
person['age'] = 26

print(person)

# Adding new values to the list
person['languages'].append('Go')

print(person)

# Delete an attribute
del person['ocupation']

print(person)

# Delete an attribute using pop method
person.pop('age')

# Get dictionary items
print(person.items())

# Get dictionary keys
print(person.keys())

# Get dictionary values
print(person.values())
