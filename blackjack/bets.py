"""
Bets class
Implementation of gambling for blackjack game
"""


class PlayerWallet:
    def __init__(self, money):
        self.wallet = int(money)  # player's current balance
        self.wager = 0            # player's current bet

# return the current balance
    def balance(self):
        return self.wallet

# set the player's wager
    def bet(self, wager):
        print(f"\nPlayer bets ${wager}\n")
        self.wager = wager

# add the wager if won
    def increase(self):
        print(f"\nWon ${self.wager}")
        self.wallet += self.wager

# subtract the wager if loss
    def decrease(self):
        print(f"\nLost ${self.wager}")
        self.wallet -= self.wager

# add 1.5x wager if Blackjack
    def blackjack(self):
        print(f"\nWon ${int(self.wager * 1.5)}")
        self.wallet += int(self.wager * 1.5)
