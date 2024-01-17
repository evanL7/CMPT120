'''
This program asks the user for an integer input in inches
and presents an output of the user's input separated into miles, yards, feet, and inches.
'''

#Ask user for integer input
num_of_inches = int(input("Please enter the number of inches: "))

#Check number of miles in input
input_miles = num_of_inches // (1760*3*12)

#Check number of yards in input
input_yards = (num_of_inches - (input_miles*1760*3*12)) // (3*12)

#Check number of feet in input
input_feet = (num_of_inches - (input_miles*1760*3*12) - (input_yards*3*12)) // 12

#Check number of inches in input
input_inches = num_of_inches - (input_miles*1760*3*12) - (input_yards*3*12) - (input_feet*12)

#Display output
print(input_miles, "mi ", input_yards, "yd ", input_feet, "' ", input_inches, '"', sep="")
