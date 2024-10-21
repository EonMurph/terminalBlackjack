class Card:
    """A single playing card.

    Attributes
    ----------
    value: int
        (read only)
            A number representing the value of the card (equal to the value of the rank but capped at 10, suit is not taken into account).
    """

    ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    suits = ["♠", "♣", "❤", "♦"]

    def __init__(self, suit: int | str, rank: int) -> None:
        """
        Parameters
        ----------
        suit: int | str
            A number or string representing the suit of the card.
                (♠: "spade" | 1, ♣: "club" | 2, ❤: "heart" | 3, ♦: "diamond" | 4)
        rank: int
            A number representing the rank of the card.
                (A: 1, J:11, Q: 12, K: 13)
        """
        if type(suit) == str:
            self._suit: int = ["spade", "club", "heart", "diamond"].index(suit.lower())
        elif type(suit) == int:
            self._suit = suit - 1

        self._rank: int = rank - 1

    @property
    def value(self) -> int:
        """The value of the playing card."""
        return min(self._rank + 1, 10)

    def __str__(self) -> str:
        return f"{Card.ranks[self._rank]}{Card.suits[self._suit]}"


def main() -> None:
    card1 = Card(suit=1, rank=1)
    print(card1.value)


if __name__ == "__main__":
    main()
