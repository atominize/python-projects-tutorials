import random

# today's Lesson On 25th October 2020
# of naming variables ,this differs from programme to programme
# x = 0
# while x < 10:
#     print("daniel")
#     x = x + 1

randomNumber = random.randint(1, 100)
print("i have chosen a number between 1 and 100, guess it")
guessWrong = True

countAttempt = 0

while guessWrong:
    chosenNumber = int(input("guess number = "))
    countAttempt = countAttempt + 1
    if chosenNumber == randomNumber:
        print("you guess right")
        print(f"you won, you tried {countAttempt} times")
        guessWrong = False
    elif chosenNumber > randomNumber:
        print("you number is greater than the actual number")
    else:
        print("your number is less than the actual number")