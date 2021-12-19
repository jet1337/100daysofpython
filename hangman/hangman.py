# Hangman
# Try to guess the word before your guesses run out!

import requests
import random

# map pictures to dictionary to be printed each iteration
def picture(count):
    art0 = """
    art0
    """
    art1 = """
    art1
        """
    art2 = """
    art2
        """
    art3 = """
    art3
        """
    art4 = """
    art4
        """
    art5 = """
        art5
            """
    key = {0:art0, 1:art1, 2:art2, 3:art3, 4:art4, 5:art5}
    print(key[count])

# generate word from a wordlist
def get_word():
    s = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    words = s.content.splitlines()
    word = random.choice(words).decode()
    selection = []
    for letter in word:
        selection.append(letter)
    return selection

def main():
    # get the curret word
    word = get_word()
    secret_word = []
    letters = []
    count = 0
    win = False
    # make a 'blank' word
    for letter in word:
        secret_word.append("_")
    # main game loop
    while not win and count < 6:
        print(*secret_word, sep="")
        guess = input("Guess a letter: ")
        if guess in letters:
            print("Guess Again - That letter has already been guessed")
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
    # Results
    print(f"The word was {''.join(word)}")
    if win:
        print("You win!")
    else:
        print("You lose...")

if __name__ == "__main__": main()