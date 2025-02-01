from deck import Deck
from player import Player

deck = Deck()
deck.shuffle()
player1 = Player(deck)

player1.hit()

print(player1)
    