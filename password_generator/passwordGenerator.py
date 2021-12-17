# Password generator
# Function: create a random password

import random

def shuffle(input):
    random.seed(random.randint(0,42069))
    list = []
    result = ""
    for char in input:
        list.append(char)
    for i in range(0,len(list)):
        swap_index = random.randint(0,len(list)-1)
        temp = list[i]
        list[i] = list[swap_index]
        list[swap_index] = temp
    for item in list: result += item
    return result

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
            password += letters[random.randint(0,len(letters) - 1)]
        for i in range(int(nums)):
            password += numbers[random.randint(0,len(numbers) - 1)]
        for i in range(int(symbs)):
            password += symbols[random.randint(0, len(symbols) - 1)]

# Randomize the selected characters
        password = shuffle(password)
        print(f"Your new password: {password}")
# Check if user wants to quit
        new_pass = input("Would you like a different password? 'y' for Yes, anything else to quit  ").lower()
        if new_pass in ['y','yes']:
            continue
        else:
            break

if __name__ == "__main__": main()