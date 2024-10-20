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
    add_to_hand(card: Card *OR* cards: list[Card]):
        Add a single card or list of cards to the hand.
    clear_hand:
        Clear the current hand of all cards.
    """

    def __init__(self, cards: list[Card] | None = None) -> None:
        """
        Parameters
        ----------
        cards: list[Card], optional
            (default None) The cards held in the hand."""
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

    def add_to_hand(self, cards: list[Card] | Card) -> None:
        """Add a card or list of cards to the hand.

        Parameters
        ----------
        cards: (list[Card] | Card)
            The list of `Card` objects, or a just a single `Card`, to add to the hand.
        """
        if type(cards) == Card:
            self.cards.append(cards)
        elif type(cards) == list[Card]:
            self.cards += cards

    def clear_hand(self) -> None:
        """Remove and return all the cards from the hand."""
        self.cards = []


def main() -> None:
    deck = Deck()
    hand = Hand(cards=deck.deal_cards(num_cards=5))
    print(hand)
    print(hand.value)


if __name__ == "__main__":
    main()
