from random import randint

random_num = randint(1,11)
user_num = int(input('Please enter your desired Number: '))

print(f'The Random Number was {random_num} and What you guessed is {user_num}')

if random_num == user_num:
    print('Congratulations!!!!!!!!You won the game.')
elif random_num > user_num:
    print('You lose the game!! Your number {user_num} is less than {random_num}')
elif random_num < user_num:
    print('You lose the game!! Your number {user_num} is greater than {random_num}')