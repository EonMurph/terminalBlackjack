from hand import Hand
from deck import Deck
from card import Card


class Person:
    """A person in the game of blackjack.

    This class is not be instantiated,
    but instead to be inherited by the player and dealer classes.

    Attributes
    ----------
    hand: Hand
        The persons hand of cards.
    tally: int
        The total value of the person's hand.

    Methods
    -------
        get_card(deck: Deck, num_cards: int = 1):
            Get a card from the deck and add it to the hand.
        clear_hand -> list[Card] | None:
            Remove and return all the cards in the current hand.

    """

    def __init__(self, hand: Hand | None = None) -> None:
        """
        Parameters
        ----------
        hand: Hand, optional
            (default None)
                The hand the person holds.
        """
        if hand is not None:
            self.hand: Hand = hand
        else:
            self.hand = Hand()

    @property
    def tally(self) -> int:
        return self.hand.value

    def __str__(self) -> str:
        person_string = " ".join(map(str, self.hand.cards))
        person_string += f" Tally: {self.tally}"

        if self.hand.size == 0:
            return "The hand is empty."

        return person_string

    def clear_hand(self) -> list[Card] | None:
        """Remove and return all the cards from the hand.

        Returns
        -------
        list[Card] | None:
            A list of `Card` objects after being removed from the person's hand.
        """
        cards: list[Card] = self.hand.cards
        self.hand.clear_hand()

        return cards


def main() -> None:
    deck = Deck()
    deck.shuffle_deck()
    person = Person(Hand(cards=deck.deal_cards(num_cards=5)))
    print(person)
    person.get_card(deck)
    print(person)


if __name__ == "__main__":
    main()
