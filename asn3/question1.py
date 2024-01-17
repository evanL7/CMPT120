'''
 This program uses a recursive function to encrypt a string with each letter increased by 1 letter.
 The function allows the string to have uppercase and lowercase letters of the alphabet.
'''

# This recursive function encrypts the string
def encrypt(st):
    try:
        if st.isalpha() or st == "": # This line checks if the string consists of alphabetical characters or the empty string because that is our base case
            if st == "": # This is the base case when the string is empty
                return ""
            else:
                return next_letter(st[0]) + encrypt(st[1:]) # This is the subproblem
        else: # This line here applies only when the above conditional is false which means there are characters in the string which cannot be encrypted
            print("Please ensure that the string consists of only letters of the alphabet.")
            return    
    except: # This line here applies when the user potentially enters a data type that is not a string, such as an integer or float
        print("Please ensure that the string consists of only letters of the alphabet.")
        return 

# This function takes a string argument and returns the next letter of the character
def next_letter(ch):
    letters_of_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    index_location = letters_of_alphabet.index(ch.lower()) # This line finds the corresponding index associated with the letter parameter. The lower method call is used in case the character is uppercase
    
    if ch.islower(): # If the character is lowercase, we want to maintain the formatting
        # This condition avoids the error of indexing out of range
        if letters_of_alphabet[index_location] == 'z':
            return 'a'

        # This line returns the next letter.
        return letters_of_alphabet[index_location + 1]
    
    if ch.isupper(): # If the character is uppercase, we want to maintain the formatting
        # This condition avoids the error of indexing out of range
        if letters_of_alphabet[index_location] == 'z':
            return 'A'

        # This line returns the next letter.
        return letters_of_alphabet[index_location + 1].upper() # Upper method call here because the initial character was uppercase
