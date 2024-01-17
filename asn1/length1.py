'''
This program asks for an integer input in inches and presents an output of the users input separated into miles, yards, feet, and inches.
'''
#Create variables to store the amount of miles, yards, feet, or inches to use to output the final result
input_miles = 0
input_yards = 0
input_feet = 0
input_inches = 0

#Ask user for integer input
number_of_inches = int(input("Please enter the number of inches: "))

#Apply conditionals starting with highest denomination, miles to lowest denomination, inches
#Subtract the input number from the unit amount and add to the miles, yards, feet, or inches variable

#Check if input is greater than one mile
while True:
    if number_of_inches >= (1760*3*12):
        input_miles += 1
        number_of_inches -= 1760*3*12
    else:
        break

#Check if input is greater than one yard
while True:
    if number_of_inches >= (3*12):
        input_yards += 1
        number_of_inches -= 3*12
    else:
        break

#Check if input is greater than one foot
while True:
    if number_of_inches >= 12:
        input_feet += 1
        number_of_inches -= 12
    else:
        break

#Assign remaining inches to the input_inches variable
input_inches = number_of_inches

#Print out the output
print(input_miles, "mi ", input_yards, "yd ", input_feet, "' ", input_inches, '"', sep="")
