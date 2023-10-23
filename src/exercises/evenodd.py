'''
Develop a program that read a number and show if it is even or odd.

Additional: The program should only accept positive numbers & validate the number input.
'''

while True:
    number = input('Enter a number: ')

    if not number.isnumeric():
        print('Please enter a valid number')
        continue

    # Transform the number to integer
    number = int(number)

    # Check if the number is even
    if number % 2 == 0:
        print(f'The number {number} is even')
    else:
        print(f'The number {number} is odd')
    break
