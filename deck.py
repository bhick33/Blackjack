# A class to handle the creation of a deck object comprised of 52 cards

from card import Card
from random import shuffle

class Deck:
    def __init__(self) -> None:
        SUIT = {'Hearts', 'Spades', 'Diamonds', 'Clubs'}
        RANK = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        self.all_cards = []
        
        for suit in SUIT:
            for rank in RANK:
                self.all_cards.append(Card(suit, rank))
                
    def shuffle(self) -> None:
        shuffle(self.all_cards)
        print('Deck Shuffled')
        
    def deal_one(self) -> Card:
        return self.all_cards.pop(0)
    
    def __str__(self) -> str:
        deck_str = ''
        for card in self.all_cards:
            deck_str += f"{str(card)}\n"
        return deck_str