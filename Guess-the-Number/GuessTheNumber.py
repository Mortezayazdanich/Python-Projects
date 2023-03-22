import random


number1 = random.randint(1, 100)
while True:
    guess = int(input("Please enter a number:"))
    if guess > number1:
        print("Too high")
    elif guess < number1:
        print("Too low")
    else:
        print("You got it!")
        break
print (number1)
