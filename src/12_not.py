access = False

if not access:
    print('Access denied')

access = True
print(not access)

if not access:
    print('Access denied')

# not
print('NOT AND')

print('True and True =>', not (True and True))
print('True and False =>', not (True and False))
print('False and True =>', not (False and True))
print('False and False =>', not (False and False))

stock = input('Enter the stock number => ')
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))
