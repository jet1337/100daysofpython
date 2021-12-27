# Blackjack
# Play a game of blackjack with the computer
"""
Future expansions:
1. variable deck size
2. get card artwork to actually work, to replace list representation and to look cool
3a. add betting functionality [COMPLETE]
3b. add insurance functionality for dealer showing Ace
4. test Stack implementation of the card deck (may require more memory but would be like a real deck)
"""

import random
import time
import cards
from bets import playerWallet

def deal(deck, count):
    """
    Deal specified number of cards from the deck, only choosing cards with "count">0\n
    :param deck: Dictionary with card count/values
    :param count: Number of cards to be dealt
    :return: List of cards dealt ["A", "2", etc]
    """
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


def cardValue(hand, deck):
    """
    Returns the value of the hand passed to the function\n
    Counts Aces last to ensure optimal scoring\n
    :param hand: List of cards in the hand
    :param deck: Dictionary with card count/values
    :return: Int sum of card values
    """
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


def valueCheck(value):
    """
    Checks the hand value to see if the player busted or gets 21\n
    :param value: Int Hand's current value
    :return: Boolean Stay and Bust variables
    """
    if value == 21:
        print("You have 21!")
        bust = False
        stay = True
    elif value > 21:
        bust = True
        stay = True
    else:
        bust = False
        stay = False
    return stay, bust


def dealerTurn(deck, hand, value, stay, bust):
    """
    Automates the dealer decision making after the player is finished with their turn\n
    :param deck: Dictionary, card count/values
    :param hand: List, Dealer's current hand
    :param value: Int, Dealer's current hand value
    :param stay: Bool, Dealer stay condition
    :param bust: Bool, Dealer bust condition
    :return: Finalized hand, value, stay, and bust variables
    """
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


def reshuffle(deck, count):
    """
    'Reshuffles' the deck, resetting all card-count values\n
    :param deck: Dictionary, card count/values
    :param count: Int, number of decks in play
    :return: VOID
    """
    for card in deck:
        deck[card]["count"] = 4 * count


def deckTotal(deck, count):
    """
    Checks the deck amount, if lower than 50% calls reshuffle()\n
    Timer added to create more real user experience\n
    :param deck: Dictionary, card count/values
    :param count: Int, number of decks in play
    :return: VOID
    """
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
        print("-------------------------------------------")
        time.sleep(.5)

def main():
    """
    Main Function\n
    Uses a wallet object (bets.py) to keep track of player money\n
    Will exit if player chooses to quit or player money goes to $0
    """
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
    wallet = playerWallet(500) # create a new wallet
    deck_count = 5  # total number of decks
    p_bust = False  # player loss variable
    d_bust = False  # dealer loss variable
    p_stay = False  # player stay variable
    d_stay = False  # dealer stay variable
    play = True     # keep playing variable


    # initialize the deck
    reshuffle(deck, deck_count)
    # main game loop, player continue decision at the end
    while play:
        bj = False # blackjack tracker variable
        # Tell player their balance
        print(f"Your current balance is ${wallet.balance()}")
        # Get player wager
        # Keep trying if they bet over their balance or enter invalid
        while True:
            wager = input(f"How much would you like to bet?: $")
            if wager.isnumeric():
                if int(wager) > wallet.balance():
                    print("\nYou bet more than you have - enter a valid amount\n")
                else:
                    wallet.bet(int(wager))
                    break
            else:
                print("\nEnter an integer number only\n")
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
            print(f"BLACKJACK, you were dealt {player_value}!\n")
            p_stay = True
            p_bust = False
            bj = True
            time.sleep(1)
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
            # player loses wager
            wallet.decrease()
        else:
        # player stayed
            dealer_cards, dealer_value, d_stay, d_bust = dealerTurn(deck, dealer_cards, dealer_value, d_stay, d_bust)

        # dealer busted
        if d_bust:
            print(f"The dealer busted! Their final total was {dealer_value}")
            if not p_bust:
                print(f"You won! - Your total was {player_value}")
                # increase wallet based on win
                if bj:
                    wallet.blackjack()
                else:
                    wallet.increase()

        # compare hands
        if not p_bust and not d_bust:
            # draw
            if player_value == dealer_value:
                print(f"It was a draw - Player: {player_value}, Dealer: {dealer_value}")
            # dealer wins
            elif dealer_value > player_value:
                print(f"The dealer won... - Player: {player_value}, Dealer: {dealer_value}")
                wallet.decrease()
            # player wins
            elif player_value > dealer_value:
                print(f"You won! - Player: {player_value}, Dealer: {dealer_value}")
                if bj:
                    wallet.blackjack()
                else:
                    wallet.increase()


        # Check if the player can/wants to continue
        if wallet.balance() <= 0:
            print("\nYou ran out of money! -- Restart and try again!\n")
            play = False
        else:
            keep_playing = input("\nKeep playing? 'y' or 'n': ")
            print("-------------------------------------------")
            if keep_playing == 'y':
                p_stay, p_bust, d_stay, d_bust = False, False, False, False
                deckTotal(deck, deck_count)
                play = True
            else:
                play = False
    # Final amount in wallet
    if wallet.balance() > 0:
        print(f"You walk away from the table with ${wallet.balance()}")

if __name__ == "__main__": main()