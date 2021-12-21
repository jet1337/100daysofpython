# Caesar Cipher
# Encode/decode messages with a Caesar Cipher

def caesar(message, direction, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    newMessage = ""
    if direction == "decode":
        shift *= -1
    for letter in message:
        if letter.isalpha():
            position = alphabet.index(letter.lower())
            if letter.islower():
                newMessage += alphabet[(position + shift + 26) % 26]
            else:
                newMessage += alphabet[(position + shift + 26) % 26].upper()
        else:
            newMessage += letter
    return newMessage

def main():
    print("""
   ___                                
  / __\  __ _   ___  ___   __ _  _ __ 
 / /    / _` | / _ \/ __| / _` || '__|
/ /___ | (_| ||  __/\__ \| (_| || |   
\____/  \__,_| \___||___/ \__,_||_|   
                                      
   ___  _         _                   
  / __\(_) _ __  | |__    ___  _ __   
 / /   | || '_ \ | '_ \  / _ \| '__|  
/ /___ | || |_) || | | ||  __/| |     
\____/ |_|| .__/ |_| |_| \___||_|     
          |_|                         
    """)
    while True:
        direction = input("Would you like to 'encode' or 'decode' a message?: ").lower()
        if direction == "encode" or direction == "decode":
            break
        else:
            print("\nEnter a valid option\n")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift amount: ")) % 26
    print(message)
    message = caesar(message, direction, shift)
    print(message)

if __name__ == "__main__": main()


