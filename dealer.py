from person import Person
from deck import Deck
from hand import Hand
from card import Card


class Dealer(Person):
    """A dealer in the game of blackjack.

    This class should only be instantiated once per blackjack game.

    Methods
    -------
        get_card -> Card:
            Get a card from the deck and add it to the hand.
        deal_card(person: Person):
            Deal cards from the deck.
        shuffle_cards:
            Shuffle the cards in the deck.
        add_to_deck(cards: list[Card]):
            Add a list of `Card` object to the deck.

    .. Note::
        Inherits methods and attributes from :class:`Person`.
    """

    def __init__(self, deck: Deck, hand: Hand | None = None) -> None:
        """
        Parameters
        ----------
        deck: Deck
            The deck the dealer is maintaining.
        Note
            Takes all of :class:`Person`'s parameters.
        """
        super().__init__(hand=hand)
        self._deck: Deck = deck

    def __str__(self) -> str:
        return "Dealer -> " + super().__str__()

    def get_card(self) -> Card | None:
        """Get a card from the deck and add it to the hand.

        Returns
        -------
        Card | None
            A `Card` object if cards are available, otherwise `None`.
        """
        cards = self._deck.deal_card()
        if cards is None:
            print("There are no cards left in the deck.")

        return cards

    def deal_card(self, person: Person) -> None:
        """Deal cards from the deck.

        Parameters
        ----------
        hand: Hand
            The hand to which the cards will be dealt.
        """
        card = self.get_card()
        if card is None:
            print("The deck is empty.")
            return None

        person.add_to_hand(card)

    def shuffle_cards(self) -> None:
        """Shuffle the deck of cards."""
        self._deck.shuffle_deck()

    def add_to_deck(self, cards: list[Card]) -> None:
        """Add a list of `Card` objects back to the deck.

        Usually these cards will be taken from a `Person`'s hand.

        Examples
        --------
        >>> player = Player(hand=Hand(deck.deal_cards(5)))
        >>> dealer = Dealer(deck=deck, hand=Hand([deck.deal_card() for _ in range(5)]))
        >>> cards = player.clear_hand()
        >>> if cards is not None:
        >>>     dealer.add_to_deck(cards=player.clear_hand())
        >>> else:
        >>>     print("No cards in the player's hand.")
        """
        self._deck.add_to_deck(cards=cards)
    
    def take_turn(self) -> None:
        if self.tally >= 17:
            self.in_play = False
        else:
            self.deal_card(person=self)
    
    def reset(self) -> None:
        super().reset()
        cards = self.clear_hand()
        if cards is not None:
            self.add_to_deck(cards)


def main() -> None:
    deck = Deck()
    dealer = Dealer(deck=deck, hand=Hand([deck.deal_card() for _ in range(5)]))  # type: ignore
    print(dealer)
    dealer.shuffle_cards()
    dealer.get_card()
    dealer2 = Dealer(deck=deck, hand=Hand())
    dealer.deal_card(person=dealer2)
    print(dealer2)
    print(dealer)


if __name__ == "__main__":
    main()
