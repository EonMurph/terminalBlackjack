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
    deal_card() -> Card | None:
        Remove and return the top card in the deck.
    add_to_deck(card: list[Card]):
        Add a list of cards to the deck.
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

    def deal_card(self) -> Card | None:
        """Remove and return the top card in the deck.

        If there are no cards left in the deck returns None.

        Returns
        -------
        Card:
            A `Card` object, if cards are available, otherwise `None`.
        """
        if len(self._deck) == 0:
            print("The deck is empty.")
            return None
        return self._deck.pop()

    def add_to_deck(self, cards: list[Card]) -> None:
        """Add a list of cards to the deck.

        Parameters
        ----------
        cards: list[Card]
            A list of `Card` objects to be added to the deck.
        """
        self._deck += cards


def main() -> None:
    deck = Deck()
    print(deck)
    deck.shuffle_deck()
    print(deck)


if __name__ == "__main__":
    main()
