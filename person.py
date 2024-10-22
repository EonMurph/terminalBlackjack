from hand import Hand
from deck import Deck
from card import Card


class Person:
    """A person (player or dealer) in the game of blackjack.

    This class is not be instantiated,
    but instead to be inherited by the player and dealer classes.

    Attributes
    ----------
    tally: int
        The total value of the person's hand.
    in_play: bool
        Whether or not the person is in play.

    Methods
    -------
        get_card(deck: Deck):
            Get a `Card` object from the deck and add it to the hand.
        clear_hand -> list[Card] | None:
            Remove and return all the cards in the current hand.
        add_to_hand(card: Card):
            Add a `Card` object to the hand.

    """

    def __init__(self, hand: Hand | None = None) -> None:
        """
        Parameters
        ----------
        hand: Hand, optional
            (default None)
                The hand the person holds.

        .. Note::
         Arg `hand` is only intended to be supplied during testing.
        """
        if hand is not None:
            self._hand: Hand = hand
        else:
            self._hand = Hand()
        self.in_play = True

    @property
    def tally(self) -> int:
        return self._hand.value

    def __str__(self) -> str:
        person_string = " ".join(map(str, self._hand.cards))
        person_string += f" Tally: {self.tally}"

        if self._hand.size == 0:
            return "The hand is empty."

        return person_string

    def clear_hand(self) -> list[Card] | None:
        """Remove and return all the cards from the hand.

        Returns
        -------
        list[Card] | None:
            A list of `Card` objects after being removed from the person's hand,
                or `None` if hand is empty.
        """
        cards: list[Card] = self._hand.cards
        self._hand.clear_hand()

        return cards

    def add_to_hand(self, card: Card) -> None:
        """Add cards to the hand.

        Parameters
        ----------
        card: Card
            The `Card` object to be added to the hand.
        """

        self._hand.add_to_hand(card)
    
    def reset(self) -> None:
        self.in_play = True


def main() -> None:
    deck = Deck()
    deck.shuffle_deck()
    person = Person(Hand(cards=[deck.deal_card() for _ in range(5)]))  # type: ignore
    print(person)


if __name__ == "__main__":
    main()
