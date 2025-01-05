#throughout this program, make sure to print your outputs in proper format.
#ex.) Difference: x
#Don't just print the difference, make sure you label it, so the user knows
#what the number is that you are outputting.

#import the required module(s)
import math

#greet the user to the project
#ex.) Welcome to the Simple Calculator!
print("Welcome to the Simple Calculator!")


#ask the user for two numbers, and print the sum
x = float(input("Please enter your first number: "))
y = float(input("Please enter your second number: "))
print("Sum: " + str(x+y))
print()

#ask the user for two numbers, and print the difference
x = float(input("Please enter your first number: "))
y = float(input("Please enter your second number: "))
print("Difference: " + str(x-y))
print()

#ask the user for two numbers, and print the product (multiplication)
x = float(input("Please enter your first number: "))
y = float(input("Please enter your second number: "))
print("Product: " + str(x*y))
print()

#ask the user for two numbers, and print the quotient (division)
x = float(input("Please enter your first number: "))
y = float(input("Please enter your second number: "))
print("Quotient: " + str(x/y))
print()

#ask the user for two numbers, and print the first number raised to the second
#number (exponents using math.pow(x, y))
x = float(input("Please enter your first number: "))
y = float(input("Please enter your second number: "))
print(f"{x} raised to {y}: " + str(math.pow(x, y)))
print()

#ask the user for one number, and print the absolute value (math.fabs(x))
x = float(input("Please enter a number: "))
print("Absolute value: " + str(math.fabs(x)))
print()

#ask the user for one numbers, and print the square root (math.sqrt(x))
x = float(input("Please enter a number: "))
print("Square root: " + str(math.sqrt(x)))
print()

