from deck import Deck
from player import Player
from dealer import Dealer
from display import draw_hand

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
    print("\n--- Showdown! ---")  # Visual separator
    print("Your hand:", p1.hand_value)
    print("Dealer's hand:", p2.hand_value)

    if p1.hand_value > p2.hand_value and p1.hand_value <= 21:
        print("🎉 You Win! 🎉")  # Emoji and engaging language
    elif p1.hand_value < p2.hand_value or p1.hand_value > 21:
        print("😔 You Lose! 😔")  # Emoji and engaging language
    else:
        print("🤝 It's a Draw! 🤝")  # Emoji and engaging language
        


while True:
    deck = Deck()
    try:
        player1, dealer = deal_cards(deck)  # Get player and dealer
    except Exception as e:
        print(f"An error occurred: {e}")

    # Player 1 turn
    # Player's hand
    draw_hand('Your', player1)
    while player1.hand_value < 21:
        choice = input("Hit or Stand? (h/s): ")
        if choice.lower() == 'h':
            player1.hit()
            draw_hand('Your', player1)
        elif choice.lower() == 's':
            break
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stand.")

    # Dealer turn
    draw_hand("Dealer's", dealer)
    dealer.dealer_turn()  # Call the dealer_turn method

    # Check for dealer bust
    if dealer.hand_value > 21:
        print("Dealer Busted! You Win!")
    else:
        # Check who wins
        check_cards(player1, dealer)

    answer = input("\nDo you want to play again? (y/n): ")
    while answer.lower() not in ['y', 'n']:
        print("Invalid input. Please enter 'y' or 'n'.")
        answer = input("\nDo you want to play again? (y/n): ")

    if answer.lower()!= 'y':
        break