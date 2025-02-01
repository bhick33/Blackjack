# A Class to handle the data for a card Object

class Card:
    
    def __init__(self, suit, rank):
        # Init method that constructs a card from suit, rank input and assigns a value
        # using a dictionary
        VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
                'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]
    
    def __str__(self) -> str:
        # String method that defines string output of Card class.
        return f'{self.rank} of {self.suit}'