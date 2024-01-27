'''
 This program checks user's input to validate if their name and account number exist in the text file.
'''

# This function stores the text in the text file into a list that is returned to use for future use
def change_accounts_to_list(filename):
    accounts_list = [] # This variable will be used to create a nested list
    file = open(filename,'r')
    for item in file:
        item = item.strip() # Removes any leading spaces and end of line character from each item
        if item == "": # This line ensures that empty lines in the text file are not included in the list
            continue
        item = item.split() # Splits the items separated by the space into another list
        accounts_list.append(item) # Appends to list to create a nested list for ease of access
    file.close()
    return accounts_list

# This function checks if the user's input matches the details stored in the text file
def validate_user_input(acc_list,first_name,last_name,acc_num):
    for user_details in acc_list:
        if (user_details[0] == acc_num) and (user_details[1] == first_name) and (user_details[2] == last_name):
            return True # If all of the conditions have passed, the user's input is correct and matches our records
    return False # If the for loop has exited, the user's input is not in the list

# This function runs the program
def main():
    try:
        file = "charge_accounts.txt" # Note that string may need to be changed to include the full path of the text file
        accounts_book = change_accounts_to_list(file)
    except FileNotFoundError: # This line ensures that if the charge_accounts.txt file doesn't exist, the user is informed
        print('''File not found! Please ensure there exists a "charge_accounts.txt" text file within this file's directory.''')
        return
    except: # This line captures any other potential errors that may arise.
        print("There is an error. Please check the text file.")
        return

    # These lines ask for user input
    first_name = input("Please enter your first name: ")
    first_name = first_name.strip() # In case the user accidentally added an additional space before or after their input
    last_name = input("Please enter your last name: ")
    last_name = last_name.strip() # In case the user accidentally added an additional space before or after their input
    acc_num = input("Please enter your credit card number: ")
    acc_num = acc_num.strip() # In case the user accidentally added an additional space before or after their input

    if validate_user_input(accounts_book,first_name,last_name,acc_num): # If this statement is true, run the following code and return
        print("Yes, this is a valid credit card!")
        return
    else:
        print("No, this is an invalid credit card.")
        return
    
main()
