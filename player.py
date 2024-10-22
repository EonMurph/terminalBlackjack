from person import Person
from dealer import Dealer
from hand import Hand
from deck import Deck


class Player(Person):
    """A player in the game of blackjack.

    Methods
    -------
    take_turn:
        Process the player's turn.
    reset:
        Reset the instance of the :class:`Player` class.

    .. note::
        Inherits methods and attributes from :class:`Person`.
        Overrides :class:`Person`'s `reset` method.
    """

    def __init__(self, dealer: Dealer, hand: Hand | None = None) -> None:
        """
        Parameters
        ----------
        dealer: Dealer
            The dealer of the game the player is in.
        Note
            Takes all of :class:`Person`'s parameters.
        """
        super().__init__(hand=hand)
        self._dealer = dealer

    def __str__(self) -> str:
        return "Player -> " + super().__str__()

    def _hit(self) -> None:
        """Process if the player is hitting."""
        self._dealer.deal_card(person=self)

    def _stand(self) -> None:
        """Process if the player is standing."""
        self.in_play = False

        return None

    def take_turn(self) -> None:
        """Process the player's turn."""
        if not self.in_play:
            return None

        decision = ""

        def print_menu():
            print("What would you like to do on your turn:")
            print("1. Hit")
            print("2. Stand")
            print("3. Show Menu")

        print_menu()

        while decision == "":
            decision = input("Please choose an option (1-3): ")
            print()
            match decision:
                case "1":
                    self._hit()
                case "2":
                    self._stand()
                case "3":
                    print_menu()
                    decision = ""
                case _:
                    print("Not a valid choice.")
                    print()
                    decision = ""

    def reset(self, dealer: Dealer) -> None:  # type: ignore
        """Reset the instance of the :class:`Player` class."""
        super().reset()
        cards = self.clear_hand()
        if cards is not None:
            dealer.add_to_deck(cards)


def main() -> None:
    deck = Deck()
    dealer = Dealer(deck=deck)
    player = Player(dealer=dealer)
    player.take_turn()


if __name__ == "__main__":
    main()
