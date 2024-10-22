from dealer import Dealer
from player import Player
from deck import Deck
from os import system


def round_over() -> bool:
    keep_playing = input("Keep playing (y/n): ")
    match keep_playing.lower():
        case "y" | "yes":
            playing = True
            print("Starting another round.")
            print()
        case "n" | "no":
            playing = False
            print("Quitting the game.")
            print()
        case _:
            print("Not a valid choice.")
    print()

    return playing


def reset_round(player: Player, dealer: Dealer) -> None:
    player_hand = player.clear_hand()
    if player_hand is not None:
        dealer.add_to_deck(player_hand)
    dealer_hand = dealer.clear_hand()
    if dealer_hand is not None:
        dealer.add_to_deck(dealer_hand)
    player.reset(dealer)
    dealer.reset()

    for _ in range(2):
        dealer.deal_card(player)
        dealer.deal_card(dealer)


def start_round(player: Player, dealer: Dealer) -> None:
    reset_round(player, dealer)
    system("clear")


def check_round_over(player: Player, dealer: Dealer) -> bool:
    print(player)
    print(dealer)

    if player.tally == 21:
        print("Blackjack! The player has won.")
        return True
    elif player.tally > 21:
        print("The player has gone bust. Player loses.")
        return True
    elif not player.in_play and dealer.tally >= 17:
        if dealer.tally > 21:
            print("The dealer has gone bust. Player wins.")
        elif dealer.tally == 21:
            print("The dealer has blackjack. Player loses.")
        elif dealer.tally > player.tally:
            print("The dealer is closer. Player loses.")
        elif dealer.tally < player.tally:
            print("The player is closer. Player wins.")
        else:
            print("Dealer and player are tied.")

        return True

    return False


def game_loop() -> None:
    dealer = Dealer(deck=Deck())
    dealer.shuffle_cards()
    player = Player(dealer=dealer)
    playing = True
    start_round(player, dealer)

    while playing:
        system("clear")

        print(player)
        print(dealer)
        print()
        player.take_turn()
        dealer.take_turn()
        system("clear")

        is_round_over = check_round_over(player, dealer)
        print()
        if is_round_over:
            playing = round_over()
            if playing:
                start_round(player, dealer)


def main() -> None:
    game_loop()


if __name__ == "__main__":
    main()
