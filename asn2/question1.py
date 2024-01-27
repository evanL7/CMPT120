'''
This program returns True or False depending on whether a substring is a substring of the string.
'''

def sub(string,substring):
    #This variable counts the length of the substring so that another variable can index parts of the main string
    length = len(substring)

    #Using a for loop in this situation allows us to cycle through all of the possibilites for the substring to be a part of the string.
    for i in range(len(string)):

        #This variable takes a substring of the string and changes in each iteration.
        word = string[i:i+length]

        #This line checks if the word variable is the same as the substring, if it is, returns True
        if word == substring:
            return True

    #If the for loop is exited, we then know that the substring is not a part of the string and then return False.
    return False

# Test cases and expected output
print(sub("hello","hello")) # Expected output: True
print(sub("hello","world")) # Expected output: False
print(sub("hello","el")) # Expected output: True
print(sub("hello","mello")) # Expected output: False
print(sub("hello","lo")) # Expected output: True