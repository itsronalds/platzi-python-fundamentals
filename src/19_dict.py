# Dictionary is a data structure that stores data in key-value pairs. It is mutable and unordered.

my_dict = {
    'name': 'Ronald Abu Saleh',
    'age': 25,
    'ocupation': 'Software Engineer'
}

print(my_dict)
print(type(my_dict))

# Accessing values
print(my_dict['name'])
print(my_dict['age'])
print(my_dict['ocupation'])

# Unknown values (if we use get method it will return None if the key is not found)
# print(my_dict['name1'])
print(my_dict.get('name1'))
