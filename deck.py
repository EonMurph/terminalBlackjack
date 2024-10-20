from card import Card
from random import shuffle


class Deck:
    """A deck of cards.

    Attributes:
        length (int): (read only)
            a number representing the length of the deck
    Methods:
        shuffle_deck:
            shuffle the deck of cards
        deal_cards(num_cards : int = 1) -> (list[Card] | None):
            deals the top N cards in the deck
        add_to_deck(card: Card | cards: list[Card])"
            add a single card or list of cards to the deck
    """

    def __init__(self) -> None:
        self._deck: list[Card] = [
            Card(suit=suit, rank=rank) for suit in range(1, 5) for rank in range(1, 14)
        ]

    def length(self) -> int:
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

        If no cards left in the deck returns None.

        Args:
            num_cards (int) = 1:
                the number of cards to add
        """
        if len(self._deck) == 0:
            return None
        return_cards = []
        for _ in range(num_cards):
            return_cards.append(self._deck.pop())
        return return_cards

    def add_to_deck(
        self, card: Card | None = None, cards: list[Card] | None = None
    ) -> None:
        """Add a card or set of cards to the deck.

        Args:
            card (Card | None) = None:
                a Card object to be added to the deck
            cards (list[Card] | None) = None:
                a list of Card objects to be added to the deck

            Use one or the other in a single function call.
        """
        if card is not None:
            self._deck.append(card)
        if cards is not None:
            self._deck += cards


def main() -> None:
    deck = Deck()
    print(deck)
    deck.shuffle_deck()
    print(deck)


if __name__ == "__main__":
    main()
