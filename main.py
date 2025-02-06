from deck import Deck
from player import Player


def deal_cards(deck):
    deck.shuffle()
    p1 = Player(deck)
    p2 = Player(deck)
    players = [p1, p2]
    for player in players:
        player.hit()
        player.hit()
    
    return players

def check_cards(p1, p2):
    if p1.hand_value > p2.hand_value and p1.hand_value <= 21:
        print(f"Your hand: {p1.hand_value} beats Computer's hand: {p2.hand_value}\nYou Win!")
    elif p1.hand_value < p2.hand_value or p1.hand_value > 21:
        print(f"Your hand: {p1.hand_value} loses to Computer's hand: {p2.hand_value}\nYou Lose!")
    else:
        print(f"Your hand: {p1.hand_value} and Computer's hand: {p2.hand_value}\nIt's a Draw!!")

while True:
    deck = Deck()

    player1, player2 = deal_cards(deck)
    
    answer = input("do you want to play on?")
    
    if answer.lower() == 'n':
        break
    else:
        print(check_cards(player1, player2))
