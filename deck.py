from card import Card
from random import shuffle


class Deck:
    """A deck of cards.

    Attributes
    ----------
    size : int
        A number representing the amount of cards in the deck.

    Methods
    -------
    shuffle_deck:
        Shuffle the deck of cards.
    deal_cards(num_cards: int = 1) -> list[Card] | None:
        Deals a specified number of cards from the deck.
    add_to_deck(cards: list[Card] | Card):
        Add a single card or list of cards to the deck.
    """

    def __init__(self) -> None:
        self._deck: list[Card] = [
            Card(suit=suit, rank=rank) for suit in range(1, 5) for rank in range(1, 14)
        ]

    @property
    def size(self) -> int:
        """The number of cards in the deck."""
        return len(self._deck)

    def __str__(self) -> str:
        deck_string: str = " ".join(map(str, self._deck))
        if deck_string == "":
            return "The deck is empty."
        return deck_string

    def shuffle_deck(self) -> None:
        """Shuffle the deck of cards."""
        shuffle(self._deck)

    def deal_cards(self, num_cards: int = 1) -> list[Card] | None:
        """Remove and return the top N (defaults to 1) card(s) in the deck.

        If there are no cards left in the deck returns None.

        Parameters
        ----------
        num_cards: int, optional
            (default: 1)
                The number of cards to add.

        Returns
        -------
        list[Card] | None:
            A list of `Card` objects if cards are available, otherwise `None`.
        """
        if len(self._deck) == 0:
            return None
        return_cards = []
        for _ in range(num_cards):
            return_cards.append(self._deck.pop())
        return return_cards

    def add_to_deck(self, cards: list[Card] | Card) -> None:
        """Add a card or set of cards to the deck.

        Parameters
        ----------
        cards: list[Card], Card
            A list of `Card` objects, or just a single `Card`, to be added to the deck.
        """
        if type(cards) == Card:
            self._deck.append(cards)
        elif type(cards) == list[Card]:
            self._deck += cards


def main() -> None:
    deck = Deck()
    print(deck)
    deck.shuffle_deck()
    print(deck)


if __name__ == "__main__":
    main()
