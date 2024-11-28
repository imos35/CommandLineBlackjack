import random

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

def format_hand(hand):
    """
    Formats a hand for display as a readable string.
    """
    return "\n  - " + "\n  - ".join(f"{value} of {suit}" for value, suit in hand)

def play_blackjack():
    """
    Main game function to play Blackjack
    """
    deck, players_hand, dealers_hand = shuffle_and_deal()

    while calculate_hand_value(players_hand) < 21:
        print(f"Your Hand:{format_hand(players_hand)}\nTotal: {calculate_hand_value(players_hand)}")

        hit_or_stand = input("Do you want to Hit or Stand? ").lower()

        if hit_or_stand == 'hit':
            players_hand.append(deal_cards(deck))
        elif hit_or_stand == 'stand':
            break
        else:
            print("Invalid input! Please type 'Hit' or 'Stand'.")

    while calculate_hand_value(dealers_hand) < 17:
        dealers_hand.append(deal_cards(deck))

    players_total = calculate_hand_value(players_hand)
    dealers_total = calculate_hand_value(dealers_hand)

    print(f"Dealer's Hand:{format_hand(dealers_hand)}\nTotal: {dealers_total}")
    print(f"Your Hand:{format_hand(players_hand)}\nTotal: {players_total}")

    """
    Checks if players win or lose.
    """
    if players_total > 21:
        print("You bust! Dealer wins.")
    elif dealers_total > 21 or players_total > dealers_total:
        print("You win!")
    elif players_total < dealers_total:
        print("Dealer wins!")
    else:
        print("It's a tie!")


play_blackjack()