import random
import emoji

# Initialize variables
turkey_temp = 40  # Starting temperature (refrigerated turkey)
target_temp = 165  # Target internal temperature
cooking_time = 0
final_cooking_time = 300
is_cooked = False
score = 5

print("Welcome to the Thanksgiving Turkey Cooking Simulator!")
print("\nYour goal is to cook the turkey to 165°F without overcooking it.")
print("The closer you are to the ideal tempreture... the higher you score! You begin witha a score of 5, for putting the tukey in the oven - The highest score is = 105")
basting = input("Before we begin, would you like to baste your turkey? ").lower

# Main cooking loop
while not is_cooked:
    print(f"\nCurrent turkey temperature: {turkey_temp}°F")
    print(f"Cooking time: {cooking_time} minutes")

    # Get user input
    action = input("Enter 'cook' to continue cooking, 'check' to check doneness, or 'quit' to stop: ").lower()

    if action == 'cook':
        turkey_temp += random.randint(5,15)
        cooking_time += 15
        if cooking_time >= final_cooking_time:
            print("\nThe cooking time is OVER and the turkey is burnt... any longer and the house would've burned down with it.")
            is_cooked = True

            break

        # TODO: Implement cooking logic
        # Increase turkey_temp by a random amount between 5 and 15 degrees
        # Increase cooking_time by 15 minutes
        pass

    elif action == 'check':
        if turkey_temp >= 180:
            is_cooked = True
            print("Oh no. The Turkey is overcooked and everyone's waiting hungry, at the table.")

        elif turkey_temp >= target_temp and turkey_temp <= 179 and (basting == 'yes' or 'y' or 'sure'):
            is_cooked = True
            print("\nCONGRATULATIONS! Your Turkey is perfectly cooked and flavorful!")

        elif turkey_temp >= target_temp and turkey_temp <= 179 and (basting == 'no' or 'n' or 'nope'):
            is_cooked = True
            print("CONGRATULATIONS! Your Turkey is cooked, but not as flavorful.")
            break

        else:
            print("\nThe turkey is undercooked... keep cooking!")
            # TODO: Implement logic for an undercooked turkey
            # Print a message saying the turkey needs more cooking
            pass

    elif action == 'quit':
        print("You've decided to quit cooking. Your family is disappointed!")
        break

    else:
        print("Invalid input. Please try again.")

# Final message
if is_cooked:
    if turkey_temp == target_temp:
        score += 100
        print(f"You got exactly the perfect tempreture! you're a cooking pro and your score in the kitchen is a straight {score}!")
    elif turkey_temp > target_temp and turkey_temp <= 179:
        score += 70
        print(f"You almost got the perfect tempreture! you're a cooking intermediate and your score in the kitchen is a {score}")
    elif turkey_temp >= 180:
        score += 0
        print(f"You burnt the turkey. you were no where near the ideal tempreture. You're a cooking menace and your score in the kitchen is an appauling {score}")

    print(f"\nTotal cooking time: {cooking_time} minutes")


    # TODO: Implement a for loop to print a row of turkey emojis
    # The number of emojis should be equal to cooking_time // 30
    
    num_rows = cooking_time // 30
    for i in range(1, num_rows + 1):
        print(emoji.emojize(':turkey:' * i))

    pass