
import random
random_number = random.randrange (1, 10)

x = 0
while x < 100:
    user_num = int(input('Guess the number from 1 to 10, enter your number: '))

    x = x + 1

    if user_num > random_number:
        print('Number should be lower')
    elif user_num < random_number:
        print ('Number should be bigger')
    elif user_num == random_number:
        print('You a guess, it is namber: ', user_num, 'Number of attemts = ', x)
        answer = input ('Continue ? Y/n: ')
        if answer == 'n':
            break


    






