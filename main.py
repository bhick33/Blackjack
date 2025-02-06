from deck import Deck
from player import Player
from dealer import Dealer

def deal_cards(deck):
    deck.shuffle()
    p1 = Player(deck)
    dealer = Dealer(deck)  # Create a Dealer instance
    players = [p1, dealer]
    for player in players:
        player.hit()
        player.hit()
    return p1, dealer  # Return the player and dealer

def check_cards(p1, p2):
    if p1.hand_value > p2.hand_value and p1.hand_value <= 21:
        print(f"Your hand: {p1.hand_value} beats Computer's hand: {p2.hand_value}\nYou Win!")
    elif p1.hand_value < p2.hand_value or p1.hand_value > 21:
        print(f"Your hand: {p1.hand_value} loses to Computer's hand: {p2.hand_value}\nYou Lose!")
    else:
        print(f"Your hand: {p1.hand_value} and Computer's hand: {p2.hand_value}\nIt's a Draw!!")

while True:
    deck = Deck()
    player1, dealer = deal_cards(deck)  # Get player and dealer

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

    # Dealer turn
    print("\nDealer's hand:")
    print(dealer)
    dealer.dealer_turn()  # Call the dealer_turn method

    # Check for dealer bust
    if dealer.hand_value > 21:
        print("Dealer Busted! You Win!")
    else:
        # Check who wins
        check_cards(player1, dealer)

    answer = input("\nDo you want to play again? (y/n): ")
    if answer.lower() != 'y':
        break