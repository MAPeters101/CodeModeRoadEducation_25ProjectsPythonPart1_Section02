#import the random and math module
import math
import random

print("Welcome to the lucky number generator!\n")

fName = input("Enter your first name: ") #get user input on their first name
lName = input("Enter your last name: ") #get user input on their last name
age = int(input("Enter your age: ")) #get user input on their age (remember to wrap it around an int())
fNameLen = len(fName)
lNameLen = len(lName)

x = math.fabs(fNameLen + lNameLen) #set x equal to the absolute value of THE LENGTH of fName + THE LENGTH of lName
y = random.randint(1, 100) #set y equal to a random integer between 1 and 100

#luckyNum = math.ceil(x + y + age) #set luckyNum equal to the ceiling of x + y + age
luckyNum = math.ceil((age * (fNameLen+lNameLen)) / y) #Multiply the user's age by the length of the user’s names, and divide this product by the random integer

#add luckyNum after the string
print("Your lucky number is: " + str(luckyNum))
