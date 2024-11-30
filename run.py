import random


# Deck functions for creating deck, shuffling cards and dealing

def create_deck():
    """
    Creates the deck and the cards values
    """
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    return [(value, suit) for value in values for suit in suits]


def deal_cards(deck):
    """
    Deals a card
    """
    return deck.pop()


def shuffle_and_deal():
    """
    Shuffles and deals players their hands. (Starts game)
    """
    deck = create_deck()
    random.shuffle(deck)

    players_hand = [deal_cards(deck), deal_cards(deck)]
    dealers_hand = [deal_cards(deck), deal_cards(deck)]

    return deck, players_hand, dealers_hand


def calculate_hand_value(hand):
    """
    Calculates the value of the hands dealt
    """
    total = sum(card[0] for card in hand)
    for card in hand:
        if total > 21 and card[0] == 11:
            total -= 10
    return total


# ASCII Cards

def ascii_card(value, suit):
    """
    Generates an ASCII representation of a card.
    """

    suit_symbols = {
        'Hearts': '♥',
        'Diamonds': '♦',
        'Clubs': '♣',
        'Spades': '♠'
    }

    if value == 11:
        value = 'A'
    elif value == 10:
        value = '10'
    elif value == 12:
        value = 'J'
    elif value == 13:
        value = 'Q'
    elif value == 14:
        value = 'K'

    top = " _____ "
    middle = f"|{str(value):<2}   |"
    center = f"|  {suit_symbols[suit]}  |"
    bottom = f"|   {str(value):>2}|"
    base = " ----- "

    return "\n".join([top, middle, center, bottom, base])


def ascii_hand(hand):
    """
    Generates ASCII art for a hand of cards.
    """
    ascii_cards = [ascii_card(value, suit).split("\n") for value, suit in hand]

    combined = ["".join(card_row) for card_row in zip(*ascii_cards)]

    return "\n".join(combined)


# Gameplay mechanics

def play_blackjack():
    """
    Main game function to play Blackjack
    """
    deck, players_hand, dealers_hand = shuffle_and_deal()

    while calculate_hand_value(players_hand) < 21:
        print(
            f"\nYour Hand:\n{ascii_hand(players_hand)}\n"
            f"Total: {calculate_hand_value(players_hand)}\n"
            )

        hit_or_stand = input("Do you want to Hit or Stand?\n").lower()

        if hit_or_stand == 'hit':
            players_hand.append(deal_cards(deck))
        elif hit_or_stand == 'stand':
            break
        else:
            print("\nInvalid input! Please type 'Hit' or 'Stand'.\n")

    while calculate_hand_value(dealers_hand) < 17:
        dealers_hand.append(deal_cards(deck))

    players_total = calculate_hand_value(players_hand)
    dealers_total = calculate_hand_value(dealers_hand)

    print(
        f"\nDealer's Hand:\n{ascii_hand(dealers_hand)}\n"
        f"Total: {dealers_total}\n"
        )
    print(
        f"\nYour Hand:\n{ascii_hand(players_hand)}\n"
        f"Total: {players_total}\n"
    )

    """
    Checks if players win or lose.
    """
    if players_total > 21:
        print("You bust! Dealer wins.\n")
    elif dealers_total > 21 or players_total > dealers_total:
        print("You win!\n")
    elif players_total < dealers_total:
        print("Dealer wins!\n")
    else:
        print("It's a tie!\n")


# Main Loop for game to go around smoothly

def main():
    while True:
        play_blackjack()
        while True:
            play_again = input("Want to play again? Yes or No \n").lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                print("\nThanks for playing!\n")
                return
            else:
                print("\nInvalid input! Please type 'Yes' or 'No'.\n")


main()
