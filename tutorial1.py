import random

#       First tutorials with Dan

# print("Hello World")

# firstNumber = 2
# secondNumber = 4
# result = firstNumber + secondNumber
# print(result)

# Data Types
# 1. numbers
# 2. strings

# randomNumber = random.randint(1, 100)
# print(randomNumber)

# random = input("number = ")
# print("random is " + random)

# print("Greetings World")
# print(2)
#
# number = 2
# print(number)
# firstName = "Robert"
# print(firstName)
#
# number = "Acquah"
# print(number)  # printing the stored number
#
# # this is a comment
#
# comment = """ This is the first line
# This       is         the second line
# this is the third line of the comment
# """
#
# print(comment)
#
# # comparing in python
# print(2 < 4)
# print(2 <= 4)
# print(2 > 4)
# print(2 >= 4)
# print(2 != 4)
#
# # if else statement
# if 2 > 5:
#     print("right")
# elif 2 < 5:
#     print("nothing")
# else:
#     print("wrong")

randomNumber = random.randint(1, 100)

print("I have chosen a number between 1 and 100, guess it")
chosenNumber = int(input("Guess Number = "))

if chosenNumber == randomNumber:
    print("You won, you guess right")
elif chosenNumber > randomNumber:
    print("Your number is greater than the actual number")
else:
    print("Your number is less than the actual number")
