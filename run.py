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