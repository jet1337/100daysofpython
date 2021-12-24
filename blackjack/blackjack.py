# Blackjack
# Play a game of blackjack with the computer
"""
Future expansions:
1. variable deck size
2. get card artwork to actually work, to replace list representation and to look cool
3. add betting functionality
"""

import random
import time
import cards

# Deal cards function
# input: deck and number of cards
# output: *LIST* of card names
def deal(deck, count):
    random.seed(random.randint(0,42069))
    cards = []  # Available cards
    chosen_cards = [] # Cards to return
    # add all cards with count > 0 to available cards
    for c in deck:
        if deck[c]["count"] > 0:
            cards.append(c)
    while count > 0:
        card = random.choice(cards)
        # card selected that has a count of 0
        chosen_cards.append(card)
        deck[card]["count"] -= 1
        count -= 1
    return chosen_cards

# Card value function
# input: hand & deck of cards
# output: sum of card values
# note: if an Ace valued at 11 would bust the player, auto-value to 1
def cardValue(hand, deck):
    hand_value = 0
    ace_count = 0
    # calculate the value of all non-aces
    for card in hand:
        # Keep track of number of aces in hand & skip during initial count
        if card == "A":
            ace_count += 1
            continue
        hand_value += deck[card]["value"]
    # factor in the value of the aces
    # Ace can be valued at 1 or 11
    # if hand value > 21 and Ace in hand, devalue to 1
    while ace_count > 0:
        if (hand_value + 11) > 21:
            hand_value += 1
        else:
            hand_value += 11
        ace_count -= 1
    return hand_value

# value check function
# input: player hand value
# output: booleans for stay and bust variables
def valueCheck(value):
    if value == 21:
        print("21!")
        b = False
        s = True
    elif value > 21:
        b = True
        s = True
    else:
        b = False
        s = False
    return s, b

# Dealer's turn decision function
# input: deck, dealer hand, dealer hand value, dealer stay/bust trackers
# output: dealer hand, hand value, stay/bust trackers
# note: added timer so the player could keep track of dealer actions
def dealerTurn(deck, hand, value, stay, bust):
    print("\n-- Dealer's Turn --")
    # show the dealer's hand
    print(hand, value)
    time.sleep(1.5)
    while not stay and not bust:
        # dealer must stay over 16
        if value > 16:
            stay = True
            if value <= 21:
                break
            if value > 21:
                bust = True
                break
        # deal 1 card to dealer
        hand.append(deal(deck,1)[0])
        value = cardValue(hand, deck)
        print(hand, value)
        time.sleep(1.5)
        # check if the dealer busted or hit 21
    return hand, value, stay, bust

# reshuffle function
# input: deck
# Reinitialize card counts to original values
def reshuffle(deck, count):
    for card in deck:
        deck[card]["count"] = 4 * count

# deck total function
# input: deck
# output: boolean deck status
def deckTotal(deck, count):
    total_count = 0
    for card in deck:
        total_count += deck[card]["count"]
    if total_count < int(52 * count * .5):
        print("Deck count low... Reshuffling...")
        reshuffle(deck, count)
        for i in range(3):
            print(".", end=" ")
            time.sleep(.4)
        print("\nShuffling complete!\n")
        time.sleep(.5)

# main function
def main():
    print(cards.title)
    # create a deck of cards
    deck = {
        "A":{"count":4,"value":11},
        "2":{"count":4,"value":2},
        "3":{"count":4,"value":3},
        "4":{"count":4,"value":4},
        "5":{"count":4,"value":5},
        "6":{"count":4,"value":6},
        "7":{"count":4,"value":7},
        "8":{"count":4,"value":8},
        "9":{"count":4,"value":9},
        "10":{"count":4,"value":10},
        "J":{"count":4,"value":10},
        "Q":{"count":4,"value":10},
        "K":{"count":4,"value":10}
        }
    deck_count = 1  # total number of decks
    p_bust = False  # player loss variable
    d_bust = False  # dealer loss variable
    p_stay = False  # player stay variable
    d_stay = False  # dealer stay variable
    play = True     # keep playing variable

    # initialize the deck
    reshuffle(deck, deck_count)
    # main game loop, player continue decision at the end
    while play:
        # deal dealer cards, update deck counts
        dealer_cards = deal(deck, 2)
        dealer_value = cardValue(dealer_cards, deck)
        # show player one dealer card
        print(f"\n['{dealer_cards[0]}'] Dealer is showing: {deck[dealer_cards[0]]['value']}")

        # deal player 2 cards, update deck counts
        player_cards = deal(deck, 2)
        player_value = cardValue(player_cards, deck)
        print("\n--Player's Turn--")
        print(f"{player_cards}")

        # player gets dealt 21
        if player_value == 21:
            print(f"You have {player_value}!\n")
            time.sleep(.5)
            p_stay = True
        # otherwise, let player choose
        while not p_stay and not p_bust:
            print(f"Your current hand's value is {player_value}")
            decision = input("Would you like to stay? 'y' or 'n': ")
            if decision == "y":
                p_stay = True
            else:
                print()
                # deal 1 card to player
                player_cards.append(deal(deck,1)[0])
                print(player_cards)
                player_value = cardValue(player_cards, deck)
                # check if the player busted or hit 21
                p_stay, p_bust = valueCheck(player_value)

        # player busted
        if p_bust:
            print(f"You busted!\nYour total was {player_value}")
        else:
        # player stayed
            dealer_cards, dealer_value, d_stay, d_bust = dealerTurn(deck, dealer_cards, dealer_value, d_stay, d_bust)

        # dealer busted
        if d_bust:
            print(f"The dealer busted! Their final total was {dealer_value}")
            if not p_bust:
                print(f"You won! - Your total was {player_value}")

        # compare hands
        # draw
        if not p_bust and not d_bust:
            if player_value == dealer_value:
                print(f"It was a draw - Player: {player_value}, Dealer: {dealer_value}")
            elif dealer_value > player_value:
                print(f"The dealer won... - Player: {player_value}, Dealer: {dealer_value}")
            elif player_value > dealer_value:
                print(f"You won! - Player: {player_value}, Dealer: {dealer_value}")

        # Check if the player wants to continue
        keep_playing = input("\nKeep playing? 'y' or 'n': ")
        if keep_playing == 'y':
            p_stay, p_bust, d_stay, d_bust = False, False, False, False
            deckTotal(deck, deck_count)
            play = True
        else:
            play = False


if __name__ == "__main__": main()