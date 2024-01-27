'''
This program converts a binary number into two's complement
'''

num = input("Please enter a binary number to convert to two's complement: ")

pos = 0
neg = -1
zeroes = 0

inverted = ""
neg_twos = ""

# Flips the bits
while len(num) != len(inverted):
    if num[pos] == "0":
        inverted += "1"
    else:
        inverted += "0"
    pos += 1

# Adds one to the flipped bits
while True:
    if inverted[neg] == "0":
        neg_twos = inverted[:neg] + "1" + ("0" * zeroes)
        break
    elif inverted[neg] == "1":
        neg -= 1
        zeroes += 1

print("The two's complement of", num, "is", neg_twos)
