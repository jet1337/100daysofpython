# Hangman
# Try to guess the word before your guesses run out!

import requests
import random

# map pictures to dictionary to be printed each iteration
def picture(count):
    art0 = """            
         +--------;      
         |        |      
         |        O
         |
         |
         |
         |
    _____|______________
    """
    art1 = """
         +--------;
         |        |
         |        O
         |        |
         |
         |
         |
    _____|______________
    """
    art2 = """
         +--------;
         |        |
         |        O
         |       /|
         |
         |
         |
    _____|______________
    """
    art3 = """
         +--------;
         |        |
         |        O
         |       /|\\
         |
         |
         |
    _____|______________
    """
    art4 = """
         +--------;
         |        |
         |        O
         |       /|\\
         |         \\
         |
         |
    _____|______________
    """
    art5 = """
         +--------;
         |        |
         |        O
         |       /|\\
         |       / \\
         |
         |
    _____|______________
    """
    key = {0:art0, 1:art1, 2:art2, 3:art3, 4:art4, 5:art5}
    print(key[count])

# generate word from a wordlist
def get_word():
    s = requests.get("https://www.mit.edu/~ecprice/wordlist.10000") # .100000 also available for more options
    words = s.content.splitlines()
    word = random.choice(words).decode()
    selection = []
    for letter in word:
        selection.append(letter)
    return selection

def main():
    print("""
  _                                                         
 | |__     __ _   _ __     __ _   _ __ ___     __ _   _ __  
 | '_ \   / _` | | '_ \   / _` | | '_ ` _ \   / _` | | '_ \ 
 | | | | | (_| | | | | | | (_| | | | | | | | | (_| | | | | |
 |_| |_|  \__,_| |_| |_|  \__, | |_| |_| |_|  \__,_| |_| |_|
                          |___/ 
    """)
    word = get_word()                       # get the word and create the blank version
    secret_word = ["_"] * len(word)
    letters = []
    count = 0
    win = False
    while not win and count < 6:            # main game loop
        print(*secret_word, sep="")
        guess = input("Guess a letter: ").lower()
        if guess in letters:
            print("Guess Again - That letter has already been guessed\n")
            continue
        if not guess.isalpha():
            print("Only letters are valid for this game...\n")
            continue
        letters.append(guess)
        if guess not in word:               # incorrect guess
            picture(count)
            count += 1
        else:
            for i in range(len(word)):      # correct guess
                if word[i] == guess:
                    secret_word[i] = guess
        if secret_word == word:             # end condition
            win = True
            break
    print(f"\nThe word was {(''.join(word)).upper()}")  # results
    if win:
        print("You win!")
    else:
        print("You lose...")

if __name__ == "__main__": main()