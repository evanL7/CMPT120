'''
 This program uses a function that takes a string of binary digits as an argument and returns its base 10 representation.
'''

def binary(st):
    try: # This try/except block checks if the argument entered by the user is correct, that is, a string of binary digits
        for num in range(len(st)):
            if st[num] == '1' or st[num] == '0':
                continue
            else: # This line applies if the user enters a string of digits that are not binary digits
                print("Please ensure that the string consists of only binary digits.")
                return 
    except TypeError: # This line applies if the user enters a different data type other than a string
        print("Wrong data type! Please ensure that the string consists of binary digits.")
        return 
    except: # This line covers any other errors that may potentially arise
        print("Please ensure that the string consists of only binary digits.")
        return 

    tot = 0 # Accumulator variable
    index_count = 0 # This variable will be used to keep track of the index position of the string

    # This for loop counts in descending order because we want to accumulate the variable 
    # starting from the leftmost position to the rightmost position
    for n in range(len(st)-1,-1,-1): 
        if st[index_count] == '0':
            index_count += 1
            continue
        # Adds to the accumulator if the string is a one 
        # and adds two to the power of the variable n
        tot += 2 ** n
        index_count += 1

    return tot # Returns the base 10 representation of the binary string
