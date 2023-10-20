'''
Create a program that asks the user their budget in the following months: January, February and March. 
And get the average of the three months.

Make prompt validations.
'''

january_budget = None
february_budget = None
march_budget = None

while True:
    january_budget = input('Enter your budget for January: ')

    if january_budget is None and not january_budget.isnumeric():
        print('Please enter a valid number')
        continue

    february_budget = input('Enter your budget for February: ')

    if february_budget is None and not february_budget.isnumeric():
        print('Please enter a valid number')
        continue

    march_budget = input('Enter your budget for March: ')

    if march_budget is None and not march_budget.isnumeric():
        print('Please enter a valid number')
        continue
    break

total_budget = int(january_budget) + int(february_budget) + int(march_budget)
average_budget = total_budget / 3

print(f'Your average budget is: ${str(average_budget)}')
