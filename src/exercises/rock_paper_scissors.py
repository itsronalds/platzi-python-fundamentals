import random

user_lives = 3
pc_lives = 3

while True:
    user_input = input('''
    1. Rock
    2. Paper
    3. Scissors
    
    Select an option: ''')

    # Validate user input
    if not user_input.isnumeric() or not isinstance(int(user_input), int) or int(user_input) not in [1, 2, 3]:
        print('\nPlease enter a correct option.')
        continue

    user_input = int(user_input)
    pc_input = random.randint(1, 3)

    # Print user and pc choices
    if user_input == pc_input:
        print('\nIt\'s a tie!')
        continue
    elif (user_input == 1 and pc_input == 3) or (user_input == 2 and pc_input == 1) or (user_input == 3 and pc_input == 2):
        print('\nYou win!')
        pc_lives -= 1
    else:
        print('\nYou lose!')
        user_lives -= 1

    # Check who wins
    if user_lives == 0:
        print('\nYou lose the game!')
        break
    elif pc_lives == 0:
        print('\nYou win the game!')
        break
