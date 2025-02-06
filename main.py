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

    # Player 1 turn
    print("Your hand:")
    print(player1)
    while player1.hand_value < 21:
        choice = input("Hit or Stand? (h/s): ")
        if choice.lower() == 'h':
            player1.hit()
            print("Your hand:")
            print(player1)
        else:
            break

    # Player 2 (dealer) turn (basic logic for now)
    print("\nComputer's hand:")
    print(player2)  # Show dealer's hand

    # Check for bust
    if player1.hand_value > 21:
        print("You Busted! Computer Wins!")
    else:
        # Check who wins
        check_cards(player1, player2)

    answer = input("\nDo you want to play again? (y/n): ")
    if answer.lower()!= 'y':
        break