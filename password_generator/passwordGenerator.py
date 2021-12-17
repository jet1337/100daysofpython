# Password generator
# Function: create a random password

import random

def shuffle(input):
    random.seed(random.randint(0,42069))
    list = []
    for char in input:
        list.append(char)
    random.shuffle(list)
    return list

def main():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Password generator loop
    while True:
        length = input("How long would you like your password (8-20)? ")
# Check for valid range
        if length.isnumeric():
            if int(length) not in range(8,21):
                print("Please input a valid password length")
                continue
        nums = input("How many numbers? ")
        symbs = input("How many symbols? ")
# Make sure they entered numbers only
        if not length.isnumeric() or not nums.isnumeric() or not symbs.isnumeric():
            print("Please enter valid numbers for your options")
            continue

        lets = int(length) - int(nums) - int(symbs)

# Get the characters from the corresponding lists
        password = ""
        for i in range(lets):
            password += random.choice(letters)
        for i in range(int(nums)):
            password += random.choice(numbers)
        for i in range(int(symbs)):
            password += random.choice(symbols)

# Randomize the selected characters
        password = shuffle(password)
        print("Your new password: ", *password, sep="")
# Check if user wants to quit
        new_pass = input("Would you like a different password? 'y' for Yes, anything else to quit  ").lower()
        if new_pass in ['y','yes']:
            print()
            continue
        else:
            break

if __name__ == "__main__": main()