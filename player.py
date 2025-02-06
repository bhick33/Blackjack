class Player:
    def __init__(self, deck) -> None:
        self.hand = []
        self.deck = deck
        self.hand_value = 0
    
    def hit(self) -> None:
        # A method to add a card to the hand array and update the hand value
        
        self.hand.append(self.deck.deal_one())
        self.hand_value += self.hand[-1].value
    
    def adjust_for_ace(self):
        # Adjust the Ace's value if the hand value exceeds 21
        while self.hand_value > 21 and any(card.rank == 'Ace' for card in self.hand):
            for card in self.hand:
                if card.rank == 'Ace' and card.value == 11:
                    card.value = 1
                    self.hand_value -= 10
                    break
    
    def __str__(self) -> str:
        # String method that defines string output of Hand class.
        new_str = ""
        for card in self.hand:
            new_str += str(card) + "\n"
        return f'{new_str}Hand value: {self.hand_value}'