# w3schools.com

# 1. doesn't need ; to show the end of statement
# 2. Indentation

# number = 1
#     lastName = "Robert"

print("Greetings World")


#       Variables in Python
# Python has no command for declaring a variable.

x = 5
y = "How are you?"

#       Comments in Python
# This is a comment

# Uses of comments
# 1. Comments can be used to explain Python code.
# 2. Comments can be used to make the code more readable.
# 3. Comments can be used to prevent execution when testing code.

print(y) # This is a comment

sentence = """
This is a comment
written in 
more than just one line
"""

print(sentence)

#       Creating Variables
# 1. Variables are containers for storing data values.
# 2. Unlike other programming languages, Python has no command for declaring a variable.
# 3. A variable is created the moment you first assign a value to it.
# 4. Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

#       Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
# Rules for Python variables:
# 1. A variable name must start with a letter or the underscore character
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4. Variable names are case-sensitive (age, Age and AGE are three different variables)

# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#       Output Variables
# The Python print statement is often used to output variables.
# To combine both text and a variable, Python uses the + character:
x = "awesome"
print("Python is " + x)

# You can also use the + character to add a variable to another variable:
x = "Python is "
y = "awesome"
z =  x + y
print(z)

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

