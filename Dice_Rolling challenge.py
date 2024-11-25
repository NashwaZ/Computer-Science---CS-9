import random

game = True
while game == True:
    print("Welcome to the Dice Rolling game!")

    roll = input('Do you wish to begin? yes/no: ')
    if roll == 'yes':
        d_num = random.randint(1,6)
        print('The 1st computer dice number rolled is: ',d_num)
        d_num1 = random.randint(1,6)
        print('The 2nd computer dice number rolled is: ', d_num1)
        d_nums = d_num+d_num1
        print('The computers rolled number to beat is: ', d_nums)
    elif roll == 'no':
        print("Okay then.")
        game == False
    else: 
        print("Please enter a valid input.")
        game = False

    roll2 = input('Do you wish to roll for yours? yes/no: ')
    if roll2 == 'yes' and roll == 'yes':
        d_u1 = random.randint(1,6)
        print('The  1st dice number rolled for you is: ',d_u1)
        d_u2 = random.randint(1,6)
        print('The  2nd dice number rolled for you is: ',d_u2)
        d_us = d_u1 + d_u2
        print('Your final rolled number to beat is: ', d_us)
    else:
        print('Game End.')

    if d_nums > d_us:
        print('THE COMPUTER WINS!')
    elif d_nums < d_us:
        print('YOU WON, CONGRATS')
    else:
        print("It's a draw.")
        

    










