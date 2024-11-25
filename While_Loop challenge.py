
import random

count = 0
while True:
    count+=1
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print(f'{num1} x {num2} = {num1*num2} attempt no. {count}')
    if num1 * num2 == 36:
        print("Whew!")
        break
    
    