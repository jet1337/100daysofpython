# Rock Paper Scissors
# Function: Play RPS with the computer

import random

# Generate the computer's choice
def comp_choice():
    random.seed(random.randint(0,40000))
    return random.randint(0,2)

# Check if the user wants to continue
def keep_playing():
    while True:
        decision = input("Continue Playing? 'y' or 'n': ")
        if decision == 'y':
            return True
        elif decision == 'n':
            return False
        else:
            print("Enter a valid option ('y' or 'n')")

def main():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    # Dictionary to map inputs to images
    key = {0:rock, 1:paper, 2:scissors}
    play = True
    playerScore = 0
    compScore = 0

    # Main game loop - checks for exit condition every 3 rounds
    while play:
        player = input("Enter '0' for Rock, '1' for Paper, '2' for Scissors: ")
        # Check for valid player input
        if player not in ["0","1","2"] or not str(player).isnumeric():
            print("Enter a valid choice ('0' '1' or '2')")
            continue
        player = int(player)
        # Translate decisions into images
        print(f"Player choice: {key.get(player)}")
        comp = comp_choice()
        print(f"Computer choice: {key.get(comp)}")
        # Check win/lose conditions
        if player == comp:
            print("DRAW - Try again\n")
            continue
        if player == 0 and comp == 2 or player == 2 and comp == 1 or player == 1 and comp == 0:
            print("PLAYER WINS\n")
            playerScore += 1
        else:
            print("COMPUTER WINS\n")
            compScore += 1
        print(f"Player: {playerScore} | Computer: {compScore}\n")
        # Check if player wants to quit
        if (playerScore + compScore) % 3 == 0:
            play = keep_playing()

    # Print final score
    print(f"\nThe final score is...\nPlayer: {playerScore} | Computer: {compScore}")
if __name__ == "__main__": main()