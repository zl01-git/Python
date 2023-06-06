from collections import namedtuple
from random import choice

Card = namedtuple("Card", ["rank", "shuit"])


class FrenchDeck():
    ranks = [str(rank) for rank in range(2, 11)] + list("JQKA")
    shuits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, shuit) for rank in self.ranks
                       for shuit in self.shuits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
    


deck = FrenchDeck()

shuit_values = dict(spades=3, diamonds=2, clubs=1, hearts=0)

def spades_hight(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(shuit_values) + shuit_values[card.shuit]

for card in sorted(deck, key=spades_hight):
    print(card)