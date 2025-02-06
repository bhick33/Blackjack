from player import Player

class Dealer(Player):
    def __init__(self, deck) -> None:
        super().__init__(deck)

    def dealer_turn(self):
        while self.hand_value < 17:  # Dealer hits until hand value is 17 or more
            self.hit()
            print("\nDealer hits")
            print("Dealer's hand:")
            print(self)