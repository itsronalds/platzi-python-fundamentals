from random import choice
options = ('rock', 'paper', 'scissors')

user_lives = 3
computer_lives = 3

while True:
    user_option = input('Type an option name => ').lower()
    computer_option = choice(options)

    print('User option:', user_option)
    print('Computer option:', computer_option)

    if not user_option in tuple(option.lower() for option in options):
        print('\nPlease enter a correct option.')
    elif user_option == computer_option:
        print('\nIt\'s a tie!')
    elif (user_option == options[0] and computer_option == options[2]) or (user_option == options[1] and computer_option == options[0]) or (user_option == options[2] and computer_option == options[1]):
        print('User win!')
        computer_lives -= 1
    else:
        print('Computer win!')
        user_lives -= 1

    if user_lives == 0:
        print('\nYou lose the game!')
        break
    elif computer_lives == 0:
        print('\nYou win the game!')
        break
