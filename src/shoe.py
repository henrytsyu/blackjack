import random


class Shoe:

    N_SUITS = 4
    N_DECKS = 8
    # Card values from A through K
    DEFAULT_CARDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * N_SUITS * N_DECKS

    def __init__(self):
        self.cards = Shoe.__default_cards_shuffled()

    def reset(self) -> None:
        self.cards = Shoe.__default_cards_shuffled()

    def deal(self) -> int:
        if not self.cards:
            self.reset()
        return self.card.pop()

    def __default_cards_shuffled() -> list[int]:
        cards = Shoe.DEFAULT_CARDS[:]
        random.shuffle(cards)
        return cards
