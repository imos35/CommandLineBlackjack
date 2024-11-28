import random

def create_deck():
    """
    Creates the deck and the cards values
    """
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
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

def calculate_hand_value(hand):
    total = sum(card[0] for card in hand)
    for card in hand:
        if total > 21 and card[0] == 1:
            total -= 10
    return total

while calculate_hand_value(players_hand) < 21:
    print(f'Your hand: {player_hand}, -{calculate_hand_value(player_hand)}-')

    hit_or_stand = input('Do you want to Hit or Stand?').lower()

    if hit_or_stand == 'hit':
        player_hand.append(deal_cards(deck))
        break
    elif hit_or_stand == 'stand':
        break
    else:
        print("Invalid input! Please type 'Hit' or 'Stand'.")

while calculate_hand_value(dealers_hand) < 17:
    dealers_hand.append(deal_cards(deck))



shuffle_and_deal()