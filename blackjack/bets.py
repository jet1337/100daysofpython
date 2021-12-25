"""
Bets class
Implementation of gambling for blackjack game
"""

# For wins, normal win = 1:1, blackjack = 1.5:1
class playerWallet:
    def __init__(self, money):
        self.wallet = int(money)
        self.wager = 0

    def balance(self):
        return self.wallet

    def bet(self, wager):
        print(f"\nPlayer bets ${wager}\n")
        self.wager = wager


    def increase(self):
        print(f"\nWon ${self.wager}\n")
        self.wallet += self.wager

    def decrease(self):
        print(f"\nLost ${self.wager}\n")
        self.wallet -= self.wager

    def blackjack(self, multiplier):
        print(f"Won ${self.wager * 1.5}")
        self.wallet =+ self.wager * 1.5