text = 'She know Python'
print(text[0])
print(text[1])

# ❌
# print(text[15])

# Get last character
print(text[-1])

# Other way to get last character
print(text[len(text) - 1])

# slicing
print(text[9:15])

# Get first 15 characters
print(text[:15])

print(text[4:])

print(text[::])

# Get every second character
print(text[9:15:2])
print(text[::2])
