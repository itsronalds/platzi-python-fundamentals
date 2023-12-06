if True:
    print('Should be executed')

if False:
    print('Should not be executed')

pet = input('What is your favorite pet? ')

# We need use elif because if we use three if, the program will check all the conditions
if pet == 'dog':
    print('You like dogs')
elif pet == 'cat':
    print('You like cats')
else:
    print('You like some other pet')

# ----------------------------------------------

stock = int(input('Enter the stock: '))

if stock >= 100 and stock <= 1000:
    print('The stock is correct')
else:
    print('The stock is incorrect')
