# Higher Lower
# Guess which account has more followers

import random
import art
import game_data


def getSelection():
    """
    Generate 2 random selections from game_data.py\n
    :return: 2 random selections (Dict)
    """
    data = game_data.data
    random.seed(random.randint(0, 69696969))
    # generate first person, remove from list
    person1 = random.choice(data)
    data.remove(person1)
    # generate second person
    person2 = random.choice(data)
    return person1, person2


def compare(person1, person2):
    """
    Compare two Dictionary values follower count\n
    :param person1: Dictionary, first value to compare
    :param person2: Dictionary, second value to compare
    :return: Dictionary, value with the highest follower count
    """
    if person1["follower_count"] > person2["follower_count"]:
        return person1
    else:
        return person2

def articleSelect(description):
    """
    Returns either 'A' or 'An' based on description value
    :param description: String, the description value from person dictionary
    :return: String required for correct grammar in print
    """
    if description[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        return 'an'
    else:
        return 'a'


def main():
    """
    Main Function\n
    :return: VOID
    """
    print(art.logo)
    lose = False # player loss variable
    points = 0   # player points variable
    streak = 0
    while not lose:
        # generate selections from game data
        person1, person2 = getSelection()
        # map selections to A and B
        selections = {"A":person1, "B":person2}
        print("Compare A:")
        print(f"{person1['name']}, {articleSelect(person1['description'])} {person1['description']} from {person1['country']}")
        print(art.vs)
        print("With B:")
        print(f"{person2['name']}, {articleSelect(person2['description'])} {person2['description']} from {person2['country']}\n")
        # get user guess
        while True:
            guess = input("Who has more followers? 'A' or 'B': ").upper()
            if guess not in ["A", "B"]:
                print("\nGuess only either 'A' or 'B'")
            else:
                break
        # compare two people then user guess
        correct_answer = compare(person1, person2)
        if selections[guess] == correct_answer:
            points += 1
            print(f"Correct! Current Score: {points}\n")
            streak = max(streak, points)
        else:
            print(f"\nYou lose... Your score was {points} and your longest winning streak was {streak}")
            keep_playing = input("Press enter to continue playing, or enter anything to quit: ")
            print()
            if keep_playing == "":
                points = 0
            else:
                lose = True

if __name__ == "__main__": main()