from deck import Deck
from card import Card


class Hand:
    """A hand of playing cards.

    Attributes
    ----------
    cards: list[Card]
        A list of the cards held by the hand.
    size: int
        A number representing the number of cards in the hand.
    value: int
        A number representing the value of the hand.

    Methods
    -------
    add_to_hand(card: Card):
        Add a single card to the hand.
    clear_hand:
        Remove and return all the cards from the hand.
    """

    def __init__(self, cards: list[Card] | None = None) -> None:
        """
        Parameters
        ----------
        cards: list[Card], optional
            (default None) The cards held in the hand.<br>

        .. Note::
            Param `hand` is only intended to be supplied during tests.
        """
        if cards is not None:
            self.cards: list[Card] = cards
        else:
            self.cards = []

    @property
    def size(self) -> int:
        """The number of cards in the hand."""
        return len(self.cards)

    @property
    def value(self) -> int:
        """The total value of the hand."""
        return sum([card.value for card in self.cards])

    def __str__(self) -> str:
        hand_string = " ".join(map(str, self.cards))
        hand_string += f" Value: {self.value}"
        if self.size == 0:
            return "The hand is empty."
        return hand_string

    def add_to_hand(self, card: Card) -> None:
        """Add a card to the hand.

        Parameters
        ----------
        cards: Card
            The `Card` object to add to the hand.
        """
        self.cards.append(card)

    def clear_hand(self) -> None:
        """Remove and return all the cards from the hand."""
        self.cards = []


def main() -> None:
    deck = Deck()
    cards = [deck.deal_card() for _ in range(4)]
    hand = Hand(cards=cards)  # type: ignore
    print(hand)
    print(hand.value)


if __name__ == "__main__":
    main()
