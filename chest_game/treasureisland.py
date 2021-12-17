# Treasure Island
# Function: Decision game
# Story created by Jacob Taylor

import time

def retry():
    repeat = input("Care to try again? 'y' or 'n' ").lower()
    if repeat != "y":
        return False
    else:
        print("Your eyes close, and you feel your body calling out to your spirit...\n")
        for i in range(3):
            print(". ", end="")
            time.sleep(1)
        print()
        return True


print('''
⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠉⠙⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⠉⠀⠀⠀⠀⠀⠀⠠⠀⠀⠠⠤⠌⠉⣉⣉⡙⠛⠛⠛⠛⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠉⠛⠿⣿⣿⣿⣿
⣿⣿⡿⠁⠠⠢⠀⠀⠀⠈⠑⠊⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠄⠀⠒⠀⠂⠀⠀⠂⠄⠀⠀⣍⠉⠉⠁⠀⢀⣠⣴⣶⣶⣦⡄⠉⢿⣿⣿
⣿⡿⠁⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⠀⠄⠈⠀⠀⠀⢀⣼⡟⠋⠉⠁⣩⠟⣿⡇⠘⣿⡇⣿
⣿⠁⠀⠀⠀⢀⠄⠀⣠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠄⠀⠒⠀⠀⣰⡟⣈⢹⣦⢀⣾⢳⡆⣿⢷⠀⢹⡇⣿
⣿⠀⡀⠀⠀⠂⠂⠎⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⢀⣠⡄⠀⠀⢀⠀⠀⠀⠀⠀⠀⡜⣹⠀⣿⠜⣿⠸⠙⠟⣠⣿⣞⣇⢸⣿⡇
⣿⠀⠿⠗⢦⣼⠀⠈⡀⠀⠀⠀⡄⠑⠀⠀⠀⠀⠀⠀⠀⣦⡏⡐⠁⣿⠀⠀⡐⠀⠀⠀⠀⠀⢀⢎⡼⣿⣄⠉⠀⠇⠏⠀⣈⠀⣾⣿⡇⢸⣿⡇
⡇⠀⠀⠀⠸⣿⠀⠀⢃⠀⠀⠀⠈⠣⠖⠠⠀⢀⠀⠀⣰⣿⠳⠤⢸⠂⡆⡐⠀⠀⠀⠀⠀⢀⢊⡞⠁⢀⣤⣤⠀⠀⢰⣏⠿⣰⠿⡟⡇⢸⣿
⡀⠠⠀⠒⠓⠿⠧⢀⣘⢦⡄⠀⠀⠀⠀⠀⢀⣈⣷⣾⡿⠛⠀⠠⠀⡰⣵⣁⣀⣀⠀⠀⠀⠎⡾⠀⡀⠸⠅⣿⠀⠀⢿⣤⣼⠡⢟⡠⠧⢘⡇
⣷⣶⣦⣤⣖⡢⠤⢀⣀⡈⠉⠓⣶⣾⣷⣶⣿⣿⡿⠋⢀⠠⠀⠀⣴⣿⠏⠀⠁⠸⠀⠀⡼⢸⣃⡙⣿⣶⡾⠃⣀⠀⠈⠃⠈⣩⢤⣶⣞⣿
⣿⣿⣿⠋⢿⣿⣿⣷⣶⣾⣭⣕⣒⣋⠥⠄⣀⠀⠉⠑⠂⠀⠴⠿⢏⡜⠀⠀⢀⠃⠀⢰⠇⠈⢛⠡⠃⠈⣀⣤⣴⣶⣞⣽⣵⣿⣿⣿⣿⣿
⣿⣿⣿⡆⠐⢀⣮⠝⠉⠛⢿⣿⣿⣻⣿⣷⣶⣧⣭⣂⡒⠤⠤⣀⡀⠀⠉⠀⠊⠀⠀⠋⠉⣥⡠⢤⣒⣮⣿⣿⣿⡿⣻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣇⠠⢬⣽⡇⣾⣷⣦⠻⣷⣳⠹⣿⢣⡿⣫⣿⣿⣿⣶⣦⣤⣥⣀⣒⠀⢠⣻⣯⣿⣦⡷⠛⢿⡏⢏⣎⡏⣰⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⠀⢟⡟⣷⡙⠿⠟⣷⡜⢿⡇⠀⣼⣼⡿⠋⢀⠈⠉⠻⠟⢋⢻⣿⠟⣿⣿⣿⣿⣿⣿⣧⠀⢻⡿⣿⢠⣿⣭⢹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡧⠀⢀⣻⣷⣬⣤⣿⣿⣎⠃⠀⠹⠟⣡⣶⣿⠿⣷⡀⢸⣷⠀⠈⠀⢸⡿⣿⣿⣿⠿⣿⡆⣾⠀⣿⠈⠛⠁⢾⣿⣯⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⣤⣸⠉⠍⠉⠹⠀⣿⡇⠀⠀⡴⣿⠛⡀⠀⠸⠃⡈⣿⣀⠀⠀⠀⠀⡿⡽⣱⣾⠟⢡⡟⠸⣿⣄⣤⣾⣆⡿⣻⣿⣿⣿⣿
⣿⣿⣿⣿⠇⡔⠉⢁⠁⠀⠁⠀⢀⣯⠛⠀⠀⢸⢃⢠⠘⣤⡀⣀⣿⠅⠀⠉⠀⠀⠀⡇⣇⠁⠀⢠⣾⠇⠘⠟⣿⣿⠾⠽⠁⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠋⢀⡀⣠⣀⠀⠀⠀⠀⠈⠀⠀⠀⠀⢼⡀⠀⠀⠉⠉⠁⡄⠀⠀⠀⠀⠀⡗⣩⣶⡶⠛⠁⠀⠀⠀⠃⠁⠆⠀⠣⡘⣿⣿⣿⣿⡇
⣿⣿⣿⣇⣀⣁⣾⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠸⣳⢸⡀⠂⠀⠀⠀⠀⢀⣠⣤⣠⣄⠉⢻⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⡈⠐⠠⠀⠀⠨⠀⠀⠁⢀⠀⠀⣀⣤⣶⣿⣿⣿⣷⣌⣢⣼⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⣠⠀⠀⠀⠀⠀⠐⠀⠀⢧⣯⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠆⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡼⡄⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⡀⠀⢠⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
''')                                                                       # Art created at https://www.twitchquotes.com/ascii-art-generator
print("Welcome to Treasure Island. \nYour mission is to find the treasure.\n")
win = False                                                                # Win status

while True:
    decision = ""
    print("""
    Your ship has crashed amongst the rocky shore of a foreign land.
    You awaken inside of a dimly lit cave, moonlight shining through the cracks in the cavern.
    You're already here now. As captain, you have to see this through... 
    
    To the end.
    """)
    decision = input("Ahead is a small fork in the cavern.\ngo 'left' or 'right' ").lower()          # First decision
    if decision != "left":
        print("\nYou fell into a deep hole, cracking your skull as you hit the ground.")
        repeat = retry()                                                                            # Try again?
        if repeat:
            continue
        else:
            break
    else:
        print("\nYou see a chest across the room as you squeeze through the entry into the next cavern.")
        print("""
    You feel something tug on your clothes and you hear a click.
    Water begins to rush between you and the chest, finally coming to a halt.
    You see a body of water spanning the room between you and the chest.
        """)
        decision = input("You can either 'wait' and think about the situation, or 'swim' to the treasure ").lower()  # Second decision
        if decision != "wait":
            print("\nYou decide to swim, discovering an infestation of piranhas that begin to devour you.")
            repeat = retry()  # Try again?
            if repeat:
                continue
            else:
                break
        else:
            time.sleep(4)
            print("As you ponder the situation for 10 minutes, you hear another click...")
            print("""
    You hear the sound of large rocks grinding and ropes stretching.
    The chest across the river is now crushed by a boulder, leaving no gold in the wreckage.
    To your right, what appeared to be a wall has shifted and revealed 3 doors.
    You see doors colored Red, Blue, and Yellow each with a corresponding stone button.
            """)
            decision = input("You feel this is the moment of truth.  Choose the 'Red' 'Blue' or 'Yellow' button ").lower() # Third decision
            if decision == "yellow":
                print("\nThe Yellow door opens.  You are greeted with a golden chest with blue inlays and a large ruby encrusted in the lid.")
                print("It is a bittersweet victory, but victory nonetheless.")
                win = True
                break
            elif decision == "blue":
                print("\nThe Blue door opens. Thousands of hungry rats pour out and begin to tear your flesh from bone.")
                repeat = retry()  # Try again?
                if repeat:
                    continue
                else:
                    break
            elif decision == "red":
                print("\nThe Red door opens, revealing a chest! You open the chest, only to be engulfed in flames and scorched to a crisp.")
                repeat = retry()  # Try again?
                if repeat:
                    continue
                else:
                    break
            else:
                print("\nYou die of boredom trying to decide what button to press...")
                repeat = retry()  # Try again?
                if repeat:
                    continue
                else:
                    break

if win:
    print("""
    The treasure that cost the life of your entire crew is in your grasp...
    Inside the chest is a bottle of grog that was sealed who knows when.
    You remove the cork and raise it in honor of the friends you lost on this journey.
    """)

print("\nThank you for playing!")
