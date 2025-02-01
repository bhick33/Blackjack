class Player:
    def __init__(self, deck) -> None:
        self.hand = []
        self.deck = deck
        self.hand_value = 0
    
    def hit(self) -> None:
        # A method to add a card to the hand array and update the hand value
        
        self.hand.append(self.deck.deal_one())
        self.hand_value += self.hand[-1].value
    
    def __str__(self) -> str:
        # String method that defines string output of Hand class.
        new_str = ""
        for card in self.hand:
            new_str += str(card) + "\n"
        return f'\n{new_str}\nHand value: {self.hand_value}'