import random


class Shoe:

    def __init__(self, n_suits=4, n_decks=8):
        # Card values from A through K
        self.__cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * n_suits * n_decks
        random.shuffle(self.__cards)

    def deal(self) -> int:
        if not self.__cards:
            self = Shoe()
        return self.__cards.pop()
