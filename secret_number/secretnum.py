# Secret number guessing game
# find the secret number from higher/lower clues

import random

logo = """
   ____                __     _  _            _            
  / _____ ___________ / /_   | \| |_  _ _ __ | |__ ___ _ _ 
 _\ \/ -_/ __/ __/ -_/ __/   | .` | || | '  \| '_ / -_| '_|
/___/\__/\__/_/  \__/\__/    |_|\_|\_,_|_|_|_|_.__\___|_| 
"""
# generate the secret number between 1 and 100
def secretNum():
    random.seed(random.randint(0,6969420))
    return random.randint(1, 100)

# select difficulty
# output: int guess count
def difficulty():
    level = ""
    while True:
        level = input("-Select your difficulty-\n'easy' for 10 guesses, 'hard' for 5 guesses: ").lower()
        if level not in ["easy","hard"]:
            print("Enter either 'easy' or 'hard'\n")
        else:
            break
    # 10 guesses for easy, 5 guesses for hard
    if level == "easy":
        return 10
    if level == "hard":
        return 5

# compare guess and secret number
# input: player guess, secret number
# output: boolean for win/lose variable
def numCheck(guess, secret):
    if guess == secret:
        print(f"You guessed it! The secret number was {secret}")
        return True
    elif guess < secret:
        print(f"{guess} was too low...")
        return False
    elif guess > secret:
        print(f"{guess} was too high...")
        return False

#main function
def main():
    print(logo)
    play = True # keep playing variable
    while play: # main game loop
        player_win = False  # player win tracker
        secret = secretNum()    # secret word variable
        guess_count = difficulty()  # guess counter variable
        while not player_win and guess_count > 0:
            # get user guess
            guess = input("Guess a number between 1 and 100: ")
            if not guess.isnumeric() or not int(guess) in range(1, 101):
                print("\nYou entered an invalid guess...\n")
                continue
            else:
                guess = int(guess)
            # compare guess with the secret number
            player_win = numCheck(guess, secret)
            if player_win:
                break
            # adjust guess count
            else:
                guess_count -= 1
                if guess_count > 0:
                    print(f"You have {guess_count} guesses remaining\n")
                else:
                    print(f"You have {guess_count} guesses remaining... The secret number was {secret}!")
        # ask user to play again
        play_again = input("\nPress enter to play again, or input anything to quit: ")
        print()
        if play_again != "":
            play = False

if __name__ == "__main__": main()