from deck import Deck
from card import Card


class Hand:
    """A hand of playing cards.

    Attributes:
        cards (list[Card]):
            a list of the cards held by the hand
        size (int):
            a number representing the number of cards in the hand
        value (int):
            a number representing the value of the hand
    """

    def __init__(self, cards: list[Card] | None = None) -> None:
        if cards is not None:
            self.cards: list[Card] = cards
        else:
            self.cards = []

    @property
    def size(self) -> int:
        return len(self.cards)

    @property
    def value(self) -> int:
        return sum([card.value for card in self.cards])

    def __str__(self) -> str:
        hand_string = " ".join(map(str, self.cards))
        if self.size == 0:
            return "The hand is empty."
        return hand_string

    def add_to_hand(
        self, card: Card | None = None, cards: list[Card] | None = None
    ) -> None:
        """Add a card or list of cards to the hand.

        Args:
            card (Card | None) = None:
                the single card to add to the hand
            cards (list[Card] | None) = None:
                the list of cards to add to the hand

            Use one or the other in a single function call.
        """
        if card is not None:
            self.cards.append(card)
        if cards is not None:
            self.cards += cards

    def clear_hand(self) -> None:
        """Clear the hand of all cards."""
        self.cards = []

def main() -> None:
    deck = Deck()
    hand = Hand(cards=deck.deal_cards(num_cards=5))
    print(hand)
    print(hand.value)

if __name__ == "__main__":
    main()