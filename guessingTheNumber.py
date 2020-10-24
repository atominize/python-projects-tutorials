import random

randomNumber = random.randint(1, 100)

print("I have chosen a number between 1 and 100, guess it")
chosenNumber = int(input("Guess Number = "))

if chosenNumber == randomNumber:
    print("You won, you guess right")
elif chosenNumber > randomNumber:
    print("Your number is greater than the actual number")
else:
    print("Your number is less than the actual number")
