import random

print("Welcome to Nashwa's... NUMBER GUESSING GAME!")

diff = input('To begin, choose your difficulty- easy, medium, hard: ').lower()

if diff == 'easy' or diff == 'e':
    guesses= 3
    rand_num= random.randint(0,10)
elif diff == 'medium' or diff == 'm':
    guesses = 5
    rand_num = random.randint(0,50)
elif diff == 'hard' or diff == 'h':
    guesses = 7
    rand_num = random.randint(0,100)
else:
    print("Invalid difficulty - defaulting to easy")
    guesses = 3
    rand_num = random.randint(0,10)

print(f"Lets begin, you have {guesses} guesses.")

user_g = []
for loop in range(guesses):
    u_num = int(input("Enter your guess: "))
    if u_num in user_g:
        print("You've already guessed that, please try again.")
        continue

    guesses -=1
    if u_num == rand_num:
        print(f'YOU GOT IT! In {guesses} tries!')
        break
    elif u_num > rand_num:
        print("That's a bit too high..")
    elif u_num < rand_num:
        print("That's a bit too low...")
    user_g.append(u_num)
    '/n'
    print(f"Your guesses so far - {user_g}")

    if guesses == 0:
        print(f"You are out of guesses, the number was: {rand_num}")